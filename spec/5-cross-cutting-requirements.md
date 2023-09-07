---
description: >-
  This section will highlight important requirements or describe any additional
  cross-cutting requirements that apply to this Building Block.
---

# 5 Cross-Cutting Requirements

## 5.1 Requirements

The cross-cutting requirements described in this section are an extension of the cross-cutting requirements defined in the [architecture specification document](https://govstack.gitbook.io/specification/v/1.0/architecture-and-nonfunctional-requirements). Any implementation MUST adhere to all requirements from [GovStack Security Requirements](https://govstack.gitbook.io/specification/v/1.0/security-requirements).

## 5.1.1 Privacy

Personal data MUST be kept private and never shared with any parties, except where specific authorisation has been granted. The Consent Building Block shall follow the privacy principles as laid out in the GovStack architecture.

## 5.1.2 Data Policy Audit Logging

Logs MUST be kept in a database of all created, updated, or deleted records. Logs MUST include timestamps and identify the user and affiliation that performed the transaction.

## 5.1.3 Access control (RECOMMENDED)

In general, the Consent Building Block shall follow the authentication and authorisation requirements as laid out in the [GovStack architecture](http://127.0.0.1:5000/s/39QVhd0jD6S29Isr7KGF/security-requirements/4-security-management#4.2.1.1-authentication-and-authorization). For clarity, Consent Building Block's API endpoints are invoked with a client-supplied API key which must defer to the Identification and Verification Building Block in order to verify the role and/or scope of the API key matches the API endpoint to which it is supplied. This is mentioned here, as this definition is drafted without clear guidance in the OpenAPI specification for the handling of roles and scopes.

## 5.2 Exceptions to Architectural Cross-Cutting Specifications

## 5.2.1 Privacy (REQUIRED)

In general, the Consent Building Block shall follow the authentication and authorisation requirements as laid out in the [Govstack architecture](https://govstack.gitbook.io/specification/v/1.0/security-requirements/4-security-management). For clarity, Consent Building Block's API endpoints are invoked with a client-supplied API key which MUST defer to the Identification and Verification Building Block in order to verify the role and/or scope of the API key matches the API endpoint to which it is supplied. This is mentioned here, as this Definition is drafted without clear guidance in the OpenAPI spec for the handling of roles and scopes.

## 5.3 Standards

### 5.3.1 ISO 8601

All dates should follow ISO 8601.

### 5.3.2 RFC 7159

RFC 7159 - The JavaScript Object Notation (JSON).

### 5.3.3 OpenAPI

OpenAPI Version 3.1.0.

### 5.3.4 REST API Design Guidelines Part 1

RESTful APIs follow TM Forum Specification: “REST API Design Guidelines Part 1” (requirement derived from GovStack Architecture and Nonfunctional Requirements).
