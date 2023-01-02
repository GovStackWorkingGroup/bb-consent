#!/usr/bin/env python3
from subprocess import Popen, PIPE
import csv
import os
import re
import shutil
import sys


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
  version: 1.1.0-rc1
  title: Consent BB API
  contact:
    email: balder@overtag.dk
  license:
    name: Apache 2.0
    url: 'http://www.apache.org/licenses/LICENSE-2.0.html'
tags:
  - name: org
    description: Secured operations available to organization API integration
  - name: dataconsumer
    description: Secured operations for data consumers and applications to verify consent
  - name: individual
    description: Individual operations
  - name: auditor
    description: Operations for external auditing systems to query detailed data from the system and subscribe to notifications.
  - name: notification
    description: Subscribe/unsubscribe notifications for data processors, consumers and frontend systems for individuals.
  - name: callback
    description: Callback API for other Building Blocks, especially relevant for asynchronous processes.
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
      responses:
        '200':
          description: "{responseOK}"
            {responseOK_objects}
        '400':
          description: bad input parameter
      security:
        - OAuth2: [{security}]
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

path_spec_template_post = path_spec_template + """
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/{request_parameter}'
        description: Insert manually
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
      required:
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


def get_api_spec_from_row(row, current_tag):

    url = row[0]
    method = row[1].lower()

    description = row[6].replace("\n", "\\n").replace("\"", "\\\"")
    
    # YAML quotation friendlyness: Use \n as newline characters
    # See: https://stackoverflow.com/questions/3790454/how-do-i-break-a-string-in-yaml-over-multiple-lines
    summary = row[8].replace("\n", "\\n").replace("\"", "\\\"") or description
    parameters = ""

    pattern_url_parameters = re.compile("{(\w+)}")

    # Identifier of specification usecase
    usecase = row[2].replace("\n", "\\n").replace("\"", "\\\"") or ""
    
    # Identifier of specification scenario
    scenario = row[3].replace("\n", "\\n").replace("\"", "\\\"") or ""

    sensitive = row[7] == "TRUE"

    operation_id = row[9]
    response_ok = row[10]
    security = row[11]

    for parameter in pattern_url_parameters.findall(url):
        parameters += parameter_template.format(
            where="path",
            name=parameter,
            required="true",
            schema_type="string",
            description="Unique ID of an object",
        )
    
    for query_parameter in filter(lambda x: bool(x), row[4].split(", ")):
        if query_parameter.endswith("Id"):
            parameters += parameter_template_objectid.format(
                where="query",
                name=query_parameter,
                required="true",
                description="An object with id {}".format(query_parameter),
            )
        else:
            parameters += parameter_template_schema.format(
                where="query",
                name=query_parameter,
                required="true",
                schema_model=query_parameter,
                description="An object of type {}".format(query_parameter),
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
    objects_to_return = list(filter(lambda x: bool(x), row[5].split(", ")))
    
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
schema_descriptions = {}

with open(schema_csv_file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        if is_row_with_model_name(row):
            current_model = row[0].split(": ")[-1]
            schema_descriptions[current_model] = row[3].replace("\n", "\\n").replace("\"", "\\\"")

        if current_model:
            schema_fields.setdefault(current_model, "")
            schema_field_names.setdefault(current_model, [])

        if current_model and is_row_with_schema_property(row):
            schema_field_names[current_model].append(row[0])
            schema_fields[current_model] += schema_property_template.format(
                name=row[0],
                property_type=row[1],
                format="",
                example="",
                description=row[3].replace("\n", "\\n").replace("\"", "\\\""),
            )
        elif current_model and is_row_with_schema_fk(row):
            schema_field_names[current_model].append(row[0])
            schema_fields[current_model] += schema_property_fk_template.format(
                name=row[0],
                fk_model=row[2],
            )


html_table_rows_output = ""

for schema_name, properties in schema_fields.items():
    output_schemas += schema_template.format(
        schema=schema_name,
        description=schema_descriptions[schema_name],
        schema_type="object",
        properties=properties,
        required="\n".join("           - {}".format(name) for name in schema_field_names[schema_name])
    )
    html_table_rows_output += html_table_rows_template.format(
        model_name="""<code style="font-family: monospace; white-space: nowrap">{}</code>""".format(schema_name),
        model_description=schema_descriptions[schema_name].replace("\\n", "<br>"),
        model_fields=", ".join("""<code style="font-family: monospace">{}</code>""".format(x) for x in schema_field_names[schema_name])
    )

yaml_output = template.format(paths=output_paths, schemas=output_schemas)

html_table_output = html_table_template.format(rows=html_table_rows_output)

if len(sys.argv) > 3 and sys.argv[3].strip() == "--html-table":

    print(html_table_output)

else:
    print(yaml_output)

