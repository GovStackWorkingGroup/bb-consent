---
description: >-
  This section will highlight important requirements or describe any additional
  cross-cutting requirements that apply to this Building Block.
---

# 5 Cross-Cutting Requirements

The cross-cutting requirements described in this section are an extension of the cross-cutting requirements defined in the [architecture specification document](https://govstack.gitbook.io/specification/v/1.0/architecture-and-nonfunctional-requirements). Any implementation MUST adhere to all requirements from [GovStack Security Requirements](https://govstack.gitbook.io/specification/v/1.0/security-requirements).

This section will describe any additional cross-cutting requirements for the Consent Building Block.

## 5.1 Privacy

Personal data MUST be kept private and never shared with any parties, except where specific authorisation has been granted. The Consent Building Block shall follow the privacy principles as laid out in the GovStack architecture.

## 5.2 Data Policy Audit Logging

Logs MUST be kept in a database of all created, updated, or deleted records. Logs MUST include timestamps and identify the user and affiliation that performed the transaction.

All audit logs shall be integrity protected against tampering. The Consent Building Block shall follow the data policy and audit logging requirements as laid out in the GovStack architecture.

## 5.3 Access control

In general, the Consent Building Block shall follow the authentication and authorisation requirements as laid out in the [Govstack architecture](https://govstack.gitbook.io/specification/v/1.0/security-requirements/4-security-management). For clarity, Consent Building Block's API endpoints are invoked with a client-supplied API key which MUST defer to the Identification and Verification Building Block in order to verify the role and/or scope of the API key matches the API endpoint to which it is supplied. This is mentioned here, as this Definition is drafted without clear guidance in the OpenAPI spec for the handling of roles and scopes.
