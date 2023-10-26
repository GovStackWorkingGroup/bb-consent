#!/usr/bin/env python3
import csv
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("You need to install PyYAML: pip install pyyaml")
    raise SystemExit

VERSION = "1.1.0-rc1"

if len(sys.argv) < 3:
    print("USAGE: govstack_csv_to_openapi.py <path_to_endpoint_spec.csv> <path_to_schema_spec.csv> [--html-table]")
    print("")
    print("Tip: On Linux, pipe command to `xclip -selection clipboard` to direct outputs straight into X's clipboard and then paste it.")
    print("")
    print("")
    print("Example of copying to text-only clipboard:")
    print("./govstack_csv_to_openapi.py GovStack\ Consent\ BB\ API\ endpoints\ -\ endpoints.csv GovStack\ Consent\ BB\ API\ endpoints\ -\ schema.csv | xclip -selection clipboard")
    print("")
    print("")
    print("Example of copying HTML table to html-only clipboard:")
    print("./govstack_csv_to_openapi.py GovStack\ Consent\ BB\ API\ endpoints\ -\ endpoints.csv GovStack\ Consent\ BB\ API\ endpoints\ -\ schema.csv --html-table | xclip -selection clipboard -i -t text/html")
    sys.exit(1)


class SafeDict(dict):
    """
    https://stackoverflow.com/a/17215533/405682
    """
    def __missing__(self, key):
        return '{' + key + '}'

template = """openapi: 3.0.0
servers:
  # Added by API Auto Mocking Plugin
  - description: SwaggerHub API Auto Mocking
    url: https://app.swaggerhub.com/apis/GovStack/consent-management-bb/
info:
  description: This is a basic API for GovStack's Consent Building Block. It reflects the basic requirements of the Consent BB specification, which is versioned .
  version: {VERSION}
  title: Consent BB API
  contact:
    email: balder@overtag.dk
  license:
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
tags:
  - name: config
    description: Secured operations available to organization API integration
  - name: service
    description: Secured operations for individuals, data consumers and applications to record and verify consent
  - name: auditor
    description: Operations for external auditing systems to query detailed data from the system and subscribe to notifications.
  - name: notification
    description: Subscribe/unsubscribe notifications for data processors, consumers and frontend systems for individuals.
paths:
{paths}

components:
  schemas:
{schemas}

  securitySchemes:
    OAuth2:
      type: oauth2
      flows:
        authorizationCode:
          authorizationUrl: https://example.com/oauth/authorize
          tokenUrl: https://example.com/oauth/token
          scopes:
            read: Grants global read access
            write: Grants global write access
            org: Grants access to org operations
            consumer: Grants access to data consumer operations
            individual: Grants access to specific individual read/write operations
            auditor: Grants access to specific auditor read operations

security:
  - OAuth2:
      - read
"""

path_spec_template = """
    {method}:
      tags:
        - {tag}
      summary: "{summary}"
      operationId: "{operationId}"
      description: "{description}"
      parameters: {url_parameters}
      x-specification-usecase: "{usecase}"
      x-specification-scenario: "{scenario}"
      x-specification-pii-or-sensitive: "{sensitive}"
      x-specification-crudl-model: "{crudl_model}"
      responses:
        '200':
          description: "{responseOK}"
            {responseOK_objects}
        '400':
          description: bad input parameter
      security:
        - OAuth2: [{security}]
{request_body}
"""

responseOK_template_single_object = """
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/{schema}'
"""


responseOK_template_objects = """
          content:
            application/json:
              schema:
                type: array
                items:
                  oneOf:{objects}
"""
responseOK_template_object = """
                    - $ref: '#/components/schemas/{schema}'"""

request_body_template = """
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:{request_body_parameters}{request_body_parameters_required}
"""

request_body_parameters_required_header_template = """
              required:{request_body_parameters_required}
"""

request_body_parameter_template = """
                {name}:
                  $ref: '#/components/schemas/{schema_model}'
                  description: {description}
"""

request_body_parameters_required_template = """
                - {name}
"""

# See: https://swagger.io/docs/specification/describing-parameters/
parameter_template = """
        - in: {where}
          name: "{name}"
          description: "{description}"
          required: {required}
          schema:
            type: {schema_type}
"""

# See: https://swagger.io/docs/specification/describing-parameters/
parameter_template_schema = """
        - in: {where}
          name: {name}
          description: "{description}"
          required: {required}
          schema:
            $ref: '#/components/schemas/{schema_model}'
"""

# See: https://swagger.io/docs/specification/describing-parameters/
parameter_template_objectid = """
        - in: {where}
          name: {name}
          description: "{description}"
          required: {required}
          schema:
            type: string
"""


schema_template = """
    {schema}:
      type: {schema_type}
      description: "{description}"
      x-not-in-database: {database}
{required}
      properties:
{properties}
"""


schema_property_template = """
        {name}:
          type: {property_type}
          format: "{format}"
          example: "{example}"
          description: "{description}"
"""

schema_property_fk_template = """
        {name}:
          $ref: '#/components/schemas/{fk_model}'
          x-fk-model: "{fk_model}"
          description: "{description}"
"""


django_api_template = """
# !!! This code is auto-generated, please do not modify
#
# Use the api object from the already-existing api with all
# the views that override these auto-generated views
from django.shortcuts import get_object_or_404

# Dynamic fixtures
# https://django-dynamic-fixture.readthedocs.io/en/latest/
from ddf import G

from .api import api

# Import auto-generated schemas
from . import schemas

# Import auto-generated models
from . import models

# Please note this little magic detail of django-ninja:
#
# Django Ninja will recognize that the function parameters that match path parameters should be taken from the path,
# and that function parameters that are declared with Schema should be taken from the request body.
# https://django-ninja.dev/guides/input/body/

{endpoints}
"""

django_api_get_stub_template = """
@api.get("{url}")
def {method}(request,{view_arguments}):
    return "undefined"

"""

django_api_get_object_template = """
@api.get("{url}")
def {method}(request,{view_arguments}):
    db_instance = get_object_or_404(models.{schema_name}, pk={pk_arg})
    return schemas.{schema_name}Schema.from_orm(db_instance).dict()

"""

django_api_get_object_template_2_response_objects = """
@api.get("{url}")
def {method}(request,{view_arguments}):
    db_instance = get_object_or_404(models.{schema_name}, pk={pk_arg})
    mocked_instance = G(models.{schema_name2})
    object1 = schemas.{schema_name}Schema.from_orm(db_instance).dict()
    object2 = schemas.{schema_name2}Schema.from_orm(mocked_instance).dict()
    return [object1, object2]

"""

django_api_post_template = """
@api.post("{url}")
def {method}(request,{view_arguments}):
    db_instance = models.{schema_name}.objects.create(**{schema_argument}.dict())
    return schemas.{schema_name}Schema.from_orm(db_instance).dict()

"""


django_api_post_template_empty_object = """
@api.post("{url}")
def {method}(request,{view_arguments}):
    db_instance = models.{schema_name}.objects.create()
    return schemas.{schema_name}Schema.from_orm(db_instance).dict()

"""


django_api_put_template = """
@api.put("{url}")
def {method}(request,{view_arguments}):
    return "undefined"

"""

django_api_delete_stub_template = """
@api.delete("{url}")
def {method}(request,{view_arguments}):
    return "undefined"

"""

django_api_delete_object_template = """
@api.post("{url}")
def {method}(request,{view_arguments}):
    db_instance = get_object_or_404(models.{schema_name}, pk={pk_arg})
    db_instance.delete()
    return {{"success": True}}

"""


django_admin_template = """
# !!! This code is auto-generated, please do not modify
import json

from hashlib import sha1
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

from django.core import serializers
from django.contrib import admin
from django.utils.safestring import mark_safe


from . import models


class BaseGovstackAdmin(admin.ModelAdmin):
    readonly_fields = ('serialized_snapshot', 'serialized_hash',)

    def serialized_snapshot(self, instance):

        # Convert the data to sorted, indented JSON
        response = serializers.serialize('json', [instance, ], indent=2)
        
        # Strip the list
        json_dict = json.loads(response)
        response = json.dumps(json_dict[0]["fields"], indent=2)

        # Get the Pygments formatter
        formatter = HtmlFormatter(style='colorful')

        # Highlight the data
        response = highlight(response, JsonLexer(), formatter)

        # Get the stylesheet
        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        # Safe the output
        return mark_safe(style + response)

    serialized_snapshot.short_description = 'Object as JSON artifact'

    def serialized_hash(self, instance):
        # Convert the data to sorted, indented JSON
        response = serializers.serialize('json', [instance, ], indent=2)

        # Strip the list
        json_dict = json.loads(response)
        response = json.dumps(json_dict[0]["fields"], indent=2)

        hash_value = sha1(response.encode())
        return hash_value.hexdigest()

    serialized_hash.short_description = 'hash (SHA-1 of artifact)'

{admins}
"""

django_model_admin_template = """
@admin.register(models.{schema})
class {schema}Admin(BaseGovstackAdmin):
    pass

"""

django_model_template = """
# !!! This code is auto-generated, please do not modify

from django.db import models

{models}
"""

django_schema_template = """
# !!! This code is auto-generated, please do not modify

from ninja import ModelSchema
from ninja import Schema

from . import models

{schemas}
"""

django_model_schema_template = """
class {schema}(models.Model):
    \"\"\"{description}\"\"\"
    {fields}

"""


django_api_model_schema_template = """
class {schema}Schema(ModelSchema):
    class Config:
        model = models.{schema}
        model_fields = "__all__"
"""

django_api_schema_template = """
class {schema}Schema(Schema):
{schema_fields}
"""

django_api_schema_field_template = """
    {field}: {type}
"""


django_model_charfield_template = """
    {name} = models.CharField(
        verbose_name="{name}",
        help_text="{description}",
        max_length=1024,
        null={not_required},
        blank={not_required},
    )
"""

django_model_integerfield_template = """
    {name} = models.IntegerField(
        verbose_name="{name}",
        help_text="{description}",
        null={not_required},
        blank={not_required},
    )
"""

django_model_booleanfield_template = """
    {name} = models.BooleanField(
        verbose_name="{name}",
        help_text="{description}",
        null={not_required},
        blank={not_required},
    )
"""

django_model_foreignkey_template = """
    {name} = models.ForeignKey(
        "{fk_model}",
        verbose_name="{name}",
        help_text="{description}",
        on_delete=models.PROTECT,
        null={not_required},
        blank={not_required},
    )
"""


# This table is copy-paste friendly for a Google Doc
html_table_template = """
<table style="border: 1px solid #000;">
<thead>
<tr>
<th>Model</th>
<th>Description</th>
<th>Fields</th>
</tr>
</thead>
{rows}
</table>
"""

html_table_rows_template = """
  <tr>
    <td>{model_name}</td>
    <td>{model_description}</td>
    <td>{model_fields}</td>
  </tr>
"""

html_table_cols_template = """
    
"""


def first_lowercase(string):
    return string[0].lower() + string[1:]


def get_api_spec_from_row(row, current_tag):

    url = row[0]
    method = row[1].lower()

    description = row[7].replace("\n", "\\n").replace("\"", "\\\"")
    
    # YAML quotation friendliness: Use \n as newline characters
    # See: https://stackoverflow.com/questions/3790454/how-do-i-break-a-string-in-yaml-over-multiple-lines
    summary = row[9].replace("\n", "\\n").replace("\"", "\\\"") or description
    parameters = ""
    request_body_parameters = ""
    request_body_parameters_required = ""

    pattern_url_parameters = re.compile("{(\w+)}")

    # Identifier of specification usecase
    usecase = row[2].replace("\n", "\\n").replace("\"", "\\\"") or ""
    
    # Identifier of specification scenario
    scenario = row[3].replace("\n", "\\n").replace("\"", "\\\"") or ""

    sensitive = row[8] == "TRUE"

    operation_id = row[10]
    response_ok = row[11]
    security = row[12]
    crudl_model = row[13]

    for parameter in pattern_url_parameters.findall(url):
        parameters += parameter_template.format(
            where="path",
            name=parameter,
            required="true",
            schema_type="string",
            description="Unique ID of an object",
        )
    
    for query_parameter in filter(lambda x: bool(x), row[4].split(", ")):
        # A * at the end of a query argument means "required"
        query_parameter_required = query_parameter.endswith("*")
        query_parameter_cleaned = query_parameter.rstrip("*")
        if query_parameter_cleaned.endswith("Id"):
            parameters += parameter_template_objectid.format(
                where="query",
                name=first_lowercase(query_parameter_cleaned),
                required="true" if query_parameter_required else "false",
                description="An object with id {}".format(query_parameter_cleaned),
            )
        else:
            request_body_parameters += request_body_parameter_template.format(
                name=first_lowercase(query_parameter_cleaned),
                schema_model=query_parameter_cleaned,
                description="An object of type {}".format(query_parameter_cleaned),
            )
            if query_parameter_required:
                request_body_parameters_required += request_body_parameters_required_template.format(
                    name=first_lowercase(query_parameter_cleaned),
                )

    if "List" in operation_id:
        parameters += parameter_template.format(
            where="query",
            name="offset",
            required="false",
            description="Requested index for start of resources to be provided in response requested by client",
            schema_type="integer",
        )
        parameters += parameter_template.format(
            where="query",
            name="limit",
            required="false",
            description="Requested number of resources to be provided in response requested by client",
            schema_type="integer",
        )
    
    response_ok_objects = ""
    objects_to_return = list(filter(lambda x: bool(x), row[6].split(", ")))
    
    # Single object
    if len(objects_to_return) == 1:
        if objects_to_return[0].endswith("<List>"):
            object_name = objects_to_return[0].replace("<List>", "")
            response_ok_objects = responseOK_template_objects.format(
                objects=responseOK_template_object.format(schema=object_name)
            )
        else:
            response_ok_objects = responseOK_template_single_object.format(
                schema=objects_to_return[0]
            )
    elif len(objects_to_return) > 1:
        response_ok_objects_schemas_to_insert = ""
        for return_object in objects_to_return:
            if return_object.endswith("<List>"):
                sys.stderr.write("Found an array inside an array, which is not supported, so just removing the fact that the nested object was meant as an array.")
            # We don't support arrays inside arrays currently
            return_object = return_object.replace("<List>", "")
            response_ok_objects_schemas_to_insert += responseOK_template_object.format(schema=return_object)
        response_ok_objects = responseOK_template_objects.format(
            objects=response_ok_objects_schemas_to_insert
        )

    request_body = ""
    if request_body_parameters:
        request_body_parameters_required_final = ""
        if request_body_parameters_required:
            request_body_parameters_required_final = request_body_parameters_required_header_template.format(
                request_body_parameters_required=request_body_parameters_required
            )
        request_body = request_body_template.format(
            request_body_parameters=request_body_parameters,
            request_body_parameters_required=request_body_parameters_required_final,
        )

    return {
        "url": url,
        "tag": current_tag,
        "method": method,
        "summary": summary,
        "operationId": operation_id,
        "description": description,
        "url_parameters": parameters or "[]",
        "request_parameter": "",
        "responseOK": response_ok,
        "responseOK_objects": response_ok_objects,
        "security": security,
        "usecase": usecase,
        "scenario": scenario,
        "sensitive": sensitive,
        "crudl_model": crudl_model,
        "request_body": request_body,
    }


endpoint_csv_file = sys.argv[1]
schema_csv_file = sys.argv[2]

if not os.path.exists(endpoint_csv_file):
    print("File not found: {}".format(endpoint_csv_file))

if not os.path.exists(schema_csv_file):
    print("File not found: {}".format(schema_csv_file))


def is_row_with_api_url(row):
    return "/" in row[0] and row[1]


def is_row_with_api_tag(row):
    return "API tag:" in row[0]

def is_row_with_model_name(row):
    return "Model:" in row[0]

def is_row_with_schema_property(row):
    return not is_row_with_model_name(row) and row[0] and not row[2]

def is_row_with_schema_fk(row):
    return not is_row_with_model_name(row) and row[0] and row[2]



#####################################
# PROCESS ENDPOINT CSV              #
#####################################

path_specs = {}

# Store properties of each url => {get: ..., post: ...}
endpoints = []

current_tag = None
with open(endpoint_csv_file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        if is_row_with_api_tag(row):
            current_tag = row[0].split(": ")[-1]
        if is_row_with_api_url(row):
        
            api_path = get_api_spec_from_row(row, current_tag)
        
            path = path_spec_template.format(
                **api_path
            )

            endpoints.append(api_path)

            if not api_path["url"] in path_specs:
                path_specs[api_path["url"]] = []
            path_specs[api_path["url"]].append(path)

paths_template = """
  {url}:
{path_spec}
"""

paths = {}

for url, path_spec in path_specs.items():
    if not url in paths:
        paths[url] = ""
    paths[url] += ("\n".join(path_spec))

output_paths = ""
for url, path_spec_rendered in paths.items():
    output_paths += paths_template.format(url=url, path_spec=path_spec_rendered)


#####################################
# PROCESS SCHEMA CSV                #
#####################################
models = {}

current_model = None
output_schemas = ""
schema_fields = {}
schema_field_names = {}
schema_field_names_required = {}
schema_descriptions = {}

schema_field_properties = {}

schemas_not_in_db = []

with open(schema_csv_file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        if is_row_with_model_name(row):
            schema_name = row[0].split(": ")[-1]
            if schema_name.endswith("*"):
                schema_name = schema_name[:-1]
                schemas_not_in_db.append(schema_name)
            current_model = schema_name
            schema_descriptions[current_model] = row[3].replace("\n", "\\n").replace("\"", "\\\"")

        if current_model:
            schema_fields.setdefault(current_model, "")
            schema_field_names.setdefault(current_model, [])
            schema_field_names_required.setdefault(current_model, [])
            schema_field_properties.setdefault(current_model, [])

        if current_model and is_row_with_schema_property(row):
            schema_field_names[current_model].append(row[0])
            schema_field_properties[current_model].append({
                "name": row[0],
                "type": row[1],
                "description": row[3],
            })
            if row[4] == "TRUE":
                schema_field_names_required[current_model].append(row[0])
            schema_fields[current_model] += schema_property_template.format(
                name=row[0],
                property_type=row[1],
                format="",
                example="",
                description=row[3].replace("\n", "\\n").replace("\"", "\\\""),
            )
        elif current_model and is_row_with_schema_fk(row):
            schema_field_names[current_model].append(row[0])
            schema_field_properties[current_model].append({
                "name": row[0],
                "type": "fk",
                "description": row[3],
                "fk_model": row[2],
            })
            schema_fields[current_model] += schema_property_fk_template.format(
                name=row[0],
                fk_model=row[2],
                description=row[3],
            )


html_table_rows_output = ""

for schema_name, properties in schema_fields.items():

    if schema_field_names_required[schema_name]:
        required = "\n      required:\n{required}".format(
            required="\n".join("           - {}".format(name) for name in schema_field_names_required[schema_name])
        )
    else:
        required = ""

    output_schemas += schema_template.format(
        schema=schema_name,
        description=schema_descriptions[schema_name],
        schema_type="object",
        database=str(schema_name in schemas_not_in_db).lower(),
        properties=properties,
        required=required,
    )
    html_table_rows_output += html_table_rows_template.format(
        model_name="""<code style="font-family: monospace; white-space: nowrap">{}</code>""".format(schema_name),
        model_description=schema_descriptions[schema_name].replace("\\n", "<br>"),
        model_fields=", ".join("""<code style="font-family: monospace">{}</code>""".format(x) for x in schema_field_names[schema_name])
    )


#####################################
# PROCESS OPENAPI YAML              #
#####################################

yaml_output = template.format(paths=output_paths, schemas=output_schemas, VERSION=VERSION)


def get_yaml():
    return yaml.safe_load(yaml_output)


def generate_django_models(yaml_data):
    """
    This function requires that the OpenAPI yaml has been written to disk.
    """

    django_models_output = ""

    openapi_type_to_django_map = {
        "string": django_model_charfield_template,
        "fk": django_model_foreignkey_template,
        "boolean": django_model_booleanfield_template,
        "integer": django_model_integerfield_template,
    }

    def escape_string_for_django(str_unescaped):
        return str_unescaped.replace("\"", "\\\"")

    # Auto-generated Django model output
    for schema_name, schema_fields in yaml_data["components"]["schemas"].items():

        # Skip other schemas, for instance HTTP query filters
        if schema_fields["x-not-in-database"]:
            continue

        properties_output = ""

        required_fields = schema_fields["required"]
        for field_name, field_properties in schema_fields["properties"].items():
            not_required = "True" if field_name not in required_fields else "False"
            if field_name == "id":
                # We skip ID fields, the mocking application can use Django's AutoField for this
                # It's named 'id' as well.
                continue
            if field_properties.get("x-fk-model", False):
                properties_output += django_model_foreignkey_template.format(
                    name=escape_string_for_django(field_name),
                    fk_model=field_properties["x-fk-model"],
                    property_type=openapi_type_to_django_map["fk"],
                    description=escape_string_for_django(field_properties["description"]),
                    not_required=not_required,
                )
            else:
                properties_output += openapi_type_to_django_map[field_properties["type"]].format(
                    name=escape_string_for_django(field_name),
                    description=escape_string_for_django(field_properties["description"]),
                    not_required=not_required,
                )

        django_models_output += django_model_schema_template.format(
            schema=schema_name,
            description=schema_descriptions[schema_name],
            fields=properties_output,
        )

    return django_model_template.format(models=django_models_output)


def generate_django_ninja_schemas(yaml_data):
    """
    This function requires that the OpenAPI yaml has been written to disk.
    """

    # Auto-generated django-ninja schema output
    django_schema_output = ""
    for schema_name, schema_fields in yaml_data["components"]["schemas"].items():

        # Skip other schemas, for instance HTTP query filters
        if schema_fields["x-not-in-database"]:
            schema_fields_output = ""
            for field in schema_field_properties[schema_name]:
                if not field["type"] in ("string", "boolean", "fk"):
                    raise Exception("Unhandled type {}".format(field["type"]))
                field_type = ""
                if field["type"] == "string":
                    field_type = "str"
                if field["type"] == "boolean":
                    field_type = "bool"
                if field["type"] == "fk":
                    field_type = "int"
                schema_fields_output += django_api_schema_field_template.format(
                    field=field["name"],
                    type=field_type,
                )
            django_schema_output += django_api_schema_template.format(
                schema=schema_name,
                schema_fields=schema_fields_output,
            )
        else:
            django_schema_output += django_api_model_schema_template.format(schema=schema_name)

    return django_schema_template.format(schemas=django_schema_output)


def generate_django_admin(yaml_data):
    """
    This function requires that the OpenAPI yaml has been written to disk.
    """

    # Auto-generated Django admin output
    django_admin_output = ""

    for schema_name, schema_fields in yaml_data["components"]["schemas"].items():

        # Skip other schemas, for instance HTTP query filters
        if schema_fields["x-not-in-database"]:
            continue

        django_admin_output += django_model_admin_template.format(
            schema=schema_name,
        )

    return django_admin_template.format(admins=django_admin_output)


def generate_django_ninja_api(yaml_data):
    """
    This function requires that the OpenAPI yaml has been written to disk.
    """

    django_api_output = ""

    def map_openapi_parameters_to_django_api(endpoint_parameters):
        for entry in endpoint_parameters:
            if entry[1] == {"type": "string"}:
                yield entry[0], "str", entry[2]
            elif entry[1] == {"type": "integer"}:
                yield entry[0], "int", entry[2]
            elif "$ref" in entry[1]:
                yield entry[0], "schemas." + entry[1]["$ref"].split("/")[-1] + "Schema", entry[2]
            else:
                raise RuntimeError(f"Does not understand {entry}")

    def get_crud_schema_argument_name(endpoint):
        # The first named argument of the requestBody
        # is the schema argument name
        try:
            schema_argument_name = next(
                iter(
                    endpoint["requestBody"]["content"]["application/json"]["schema"]["properties"].keys()
                )
            )
            return schema_argument_name
        except KeyError:
            return None


    def get_crud_schema_pk_argument(endpoint_parameters):
        """Returns an argument that can be assumed to be primary key"""
        if endpoint_parameters and endpoint_parameters[0][0].endswith("Id"):
            return endpoint_parameters[0][0]


    def get_crud_schema_name_return_value(response_schema):
        schema_type = response_schema.get("type")
        # Responses of tuples/lists of schema objects
        if schema_type == "array":
            for ref in response_schema.get("items", {}).get("oneOf", []):
                if "$ref" in ref:
                    yield ref["$ref"].split("/")[-1]
        # if schema_type == "string":
        #     yield "str"
        if "$ref" in response_schema:
            yield response_schema["$ref"].split("/")[-1]

    for api_url, endpoints in yaml_data["paths"].items():

        for method, endpoint in endpoints.items():

            endpoint_return_values = endpoint.get("responses", {}).get("200", {}).get("content", {}).get("application/json", {}).get("schema")
            endpoint_parameters = list((x["name"], x["schema"], x["required"]) for x in endpoint["parameters"])
            parameters = map_openapi_parameters_to_django_api(endpoint_parameters)

            crud_schema = endpoint.get("x-specification-crudl-model")

            view_arguments = []
            for parameter in parameters:
                if parameter[2]:
                    view_arguments.append(f"{parameter[0]}: {parameter[1]}")
                else:
                    view_arguments.append(f"{parameter[0]}: {parameter[1]}=None")

            snake_case_method_name = re.sub(r'(?<!^)(?=[A-Z])', '_', endpoint["operationId"]).lower()

            crud_schema_argument_name = get_crud_schema_argument_name(endpoint)
            pk_arg = get_crud_schema_pk_argument(endpoint_parameters)

            if endpoint_return_values:
                schema_names_returned = list(get_crud_schema_name_return_value(endpoint_return_values))

            if method == "get":
                if crud_schema:
                    if len(schema_names_returned) == 1:
                        django_api_output += django_api_get_object_template.format(
                            url=api_url,
                            method=snake_case_method_name,
                            view_arguments=", ".join(view_arguments),
                            schema_name=crud_schema,
                            pk_arg=pk_arg,
                        )
                    if len(schema_names_returned) == 2:
                        django_api_output += django_api_get_object_template_2_response_objects.format(
                            url=api_url,
                            method=snake_case_method_name,
                            view_arguments=", ".join(view_arguments),
                            schema_name=crud_schema,
                            schema_name2=schema_names_returned[1],
                            pk_arg=pk_arg,
                        )

                else:
                    django_api_output += django_api_get_stub_template.format(
                        url=api_url,
                        method=snake_case_method_name,
                        view_arguments=", ".join(view_arguments),
                    )
            elif method == "post":
                if crud_schema:
                    view_arguments.append(f"{crud_schema_argument_name}: schemas.{crud_schema}Schema")
                    django_api_output += django_api_post_template.format(
                        url=api_url,
                        method=snake_case_method_name,
                        view_arguments=", ".join(view_arguments),
                        schema_argument=crud_schema_argument_name,
                        schema_name=crud_schema,
                    )
                else:
                    django_api_output += django_api_post_template_empty_object.format(
                        url=api_url,
                        method=snake_case_method_name,
                        view_arguments=", ".join(view_arguments),
                        schema_name="TBD",
                    )

            elif method == "put":
                view_arguments.append(f"{crud_schema_argument_name}: schemas.{crud_schema}Schema")
                django_api_output += django_api_put_template.format(
                    url=api_url,
                    method=snake_case_method_name,
                    view_arguments=", ".join(view_arguments),
                )
            elif method == "delete":
                if crud_schema:
                    django_api_output += django_api_delete_object_template.format(
                        url=api_url,
                        method=snake_case_method_name,
                        view_arguments=", ".join(view_arguments),
                        pk_arg=pk_arg,
                        schema_name=crud_schema,
                    )
                else:
                    django_api_output += django_api_delete_stub_template.format(
                        url=api_url,
                        method=snake_case_method_name,
                        view_arguments=", ".join(view_arguments),
                    )

    return django_api_template.format(endpoints=django_api_output, VERSION=VERSION)



def generate_gitbook_api_spec(yaml_data):
    """
    Generates .md data for GitBook
    """

    gitbook_output = ""

    output_by_spec = {
        "config": [],
        "service": [],
        "audit": [],
        "notification": [],
        "status": [],
    }

    for api_url, endpoints in yaml_data["paths"].items():

        for method, endpoint in endpoints.items():
            section = api_url.split("/")[1]
            if not section in output_by_spec:
                raise Exception(section)
            output_by_spec[section].append(
                """
{{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/{version}/api/consent-openapi.yaml" path="{url}" method="{method}" %}}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/{version}/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/{version}/api/consent-openapi.yaml)
{{% endswagger %}}""".format(
                    url=api_url,
                    method=method,
                    version=VERSION
                )
            )

    print("""

# 8.1 API specification

The following is an automated rendition of our latest [OpenAPI YAML specification](https://github.com/GovStackWorkingGroup/bb-consent/tree/{version}/api).
""".format(version=VERSION))

    print("""
## 8.1.1 Config APIs""")

    for output in output_by_spec["config"]:
        print(output)

    print("""
## 8.1.2 Service APIs""")

    for output in output_by_spec["service"]:
        print(output)

    print("""
## 8.1.3 Audit APIs""")

    for output in output_by_spec["audit"]:
        print(output)

html_table_output = html_table_template.format(rows=html_table_rows_output)

if len(sys.argv) > 3 and sys.argv[3].strip() == "--html-table":

    print(html_table_output)

elif len(sys.argv) > 3 and sys.argv[3].strip() == "--django-models":

    output = generate_django_models(get_yaml())
    print(output)

elif len(sys.argv) > 3 and sys.argv[3].strip() == "--django-ninja-schemas":

    output = generate_django_ninja_schemas(get_yaml())
    print(output)

elif len(sys.argv) > 3 and sys.argv[3].strip() == "--django-admin":

    output = generate_django_admin(get_yaml())
    print(output)

elif len(sys.argv) > 3 and sys.argv[3].strip() == "--django-api":

    output = generate_django_ninja_api(get_yaml())
    print(output)

elif len(sys.argv) > 3 and sys.argv[3].strip() == "--gitbook-api-spec":

    output = generate_gitbook_api_spec(get_yaml())
    print(output)

else:
    print(yaml_output)
