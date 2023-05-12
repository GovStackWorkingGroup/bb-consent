---
description: >-
  This section will highlight important requirements or describe any additional
  cross-cutting requirements that apply to this Building Block.
---

# 5 Cross-Cutting Requirements

## 5.1 Data Policy Audit Logging (REQUIRED)

Logs must be kept in a database of all created, updated, or deleted records. Logs must include timestamps and identify the user and affiliation that performed the transaction.

All audit logs shall be integrity protected against tampering. The Consent Building Block shall follow the data policy and audit logging requirements as laid out in the GovStack architecture.

## 5.2 Access control (RECOMMENDED)

In general, the Consent Building Block shall follow the authentication and authorisation requirements as laid out in the [GovStack architecture](http://localhost:5000/s/39QVhd0jD6S29Isr7KGF/security-requirements/4-security-management#4.2.1.1-authentication-and-authorization). For clarity, Consent Building Block's API endpoints are invoked with a client-supplied API key which must defer to the Identification and Verification Building Block in order to verify the role and/or scope of the API key matches the API endpoint to which it is supplied. This is mentioned here, as this definition is drafted without clear guidance in the OpenAPI specification for the handling of roles and scopes.

## Exceptions to Architectural Cross-Cutting Specifications

## 5.1 Privacy (REQUIRED)

Personal data must be kept private and never shared with any parties, except where specific authorisation has been granted. The Consent Building Block shall follow the privacy principles as laid out in the GovStack architecture.
