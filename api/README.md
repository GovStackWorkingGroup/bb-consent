# Generating OpenAPI spec and Django models

Currently, we maintain our API spec in a Google Spreadsheet:
https://docs.google.com/spreadsheets/d/1snIszqyTGYk1u25liwQ_1jONTsQeH7D8aqv1Td74xt4/edit#gid=0

We use a custom script `govstack_csv_to_openapi.py` to export CSV data generated from the spreadsheet.

1. Export relevant **endpoint** tab to `GovStack Consent BB API endpoints - endpoints.csv`
2. Export relevant **schema** tab to `GovStack Consent BB API endpoints - schema.csv`
3. Run script to generate YAML/HTML/Django models.

To generate OpenAPI yaml:

```
./govstack_csv_to_openapi.py GovStack\ Consent\ BB\ API\ endpoints\ -\ endpoints.csv GovStack\ Consent\ BB\ API\ endpoints\ -\ schema.csv > consent-openapi.yaml
```


To generate Django models:

```
./govstack_csv_to_openapi.py GovStack\ Consent\ BB\ API\ endpoints\ -\ endpoints.csv GovStack\ Consent\ BB\ API\ endpoints\ -\ schema.csv --django-models > ../examples/mock/djangoapp/consentbb/app/models.py
```