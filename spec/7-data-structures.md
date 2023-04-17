---
description: >-
  This section provides information on the core data structures/data models that
  are used by this Building Block.
---

# 7 Data Structures

## 7.1 Resource Model

The resource model shows the relationship between data objects that are used by this Building Block. Data objects are ultimately modelled as OpenAPI schemas, however as the relational model isn’t easy to understand from OpenAPI specification, we start by presenting two high-level Resource Models.

### 7.1.1 Simplified Resource Model

When an individual gives consent, it is implied that the Organisation from one side and the Individual from the other side digitally sign a Consent Agreement and a respective Consent Record is created. The alternative scenario may be that signing takes place offline on a paper, but in this case, for the Consent Building Block to function properly, it is the responsibility of the Organisation to digitise (e.g. scan) the signed document and create digitally signed artefact to represent the Consent Record.

This Consent Record is a digital instance referencing the Agreement which is consented to or subsequently has consent withdrawn from.

<figure><img src="diagrams/Consent Mangement BB Simplified resource relationship model.drawio.png" alt=""><figcaption><p><a href="https://github.com/GovStackWorkingGroup/bb-consent/tree/main/spec/diagrams">Diagram Source</a></p></figcaption></figure>

### 7.1.2 Elaborated Resource Model

This model expands the relationships between resources.

Revisions are maintained for Consent Records + Agreements and Data Policies, together with cryptographic signatures. This means that all changes are captured for auditability.

For a configured Agreement, data elements requiring consent are individually specified as Agreement Data. Agreement Data is not directly relatable to processes and internals of an external system. This architectural choice gives the consent model flexibility and greatly simplifies the architecture and consent lifecycle, but it does not contradict any additional features, allowing for relations to external systems.

<figure><img src="diagrams/Consent Mangement BB Extended resource relationship model.drawio.png" alt=""><figcaption><p> <a href="https://github.com/GovStackWorkingGroup/bb-consent/tree/main/spec/diagrams">Diagram Source</a></p></figcaption></figure>

* Individual changes Consent Record.
* Individual withdraws/revokes Consent Agreement.
* Consent Record expires.
* Consent Record expiry date changes.
* Organisation replaces Consent Agreement.
* Organisation replaces Data Policy.
* Individual gives access to citizen data, using a third-party user interface (Consumer’s user interface). Example: COVID passports.

The following standards are applicable to data structures in the Registration Building Block:

* All dates should follow ISO 8601.
* RFC 7159 - The JavaScript Object Notation (JSON).
* OpenAPI Version 3.1.0.
* RESTful APIs follow TM Forum Specification: “REST API Design Guidelines Part 1” (requirement derived from GovStack Architecture and Nonfunctional Requirements).

## 7.2 Data models

Data models are defined in [Appendix A: Data models](appendix-a-data-models.md#10-appendix-a-data-models). This specification is seen as a minimum requirement, all further implementations may add more structure but should not compromise the minimal integrity laid out. All property types are generic, and a concrete implementation may add further specificity to these models.

The OpenAPI definition file is maintained in YAML format, and OpenAPI schemas may be interactively explored in the [next section](8-service-apis.md).

### 7.2.1 Individual

**Description:** Shallowly models an Individual which may reference some instance in an external system (registration system, functional ID, foundational ID etc.). An Individual instance of this model is not to be mistaken for a unique natural individual. It is up to the system owner to decide if this record permits mapping to a natural individual and/or if a single Individual row can map to several consent agreements.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td>The unique ID of an Individual row.</td><td></td><td> </td><td>PK</td><td>Y</td></tr></tbody></table>

### 7.2.2 Agreement

**Description:** An agreement contains the specification of a single purpose that can be consented to. An Agreement is universal and can be consented to by many individuals through a ConsentRecord.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>version</td><td>string</td><td>The version of this specification to which a receipt conforms.</td><td></td><td> </td><td>Uniq</td><td>Y</td></tr><tr><td>policy</td><td>fk</td><td>Reference to the policy under which this Agreement shall be governed.</td><td>fk: Policy</td><td> </td><td> </td><td>Y</td></tr><tr><td>purpose</td><td>fk</td><td>Purpose of data processing or purpose of consent. Displayed to the user.</td><td>fk: AgreementPurpose</td><td> </td><td> </td><td>Y</td></tr><tr><td>lawful_basis</td><td>string</td><td>Lawful basis of the agreement - consent / legal_obligation / contract / vital_interest / public_task / legitimate_interest.</td><td></td><td></td><td></td><td></td></tr><tr><td>dpia</td><td>string</td><td>Data Protection Impact Assessment.</td><td></td><td></td><td></td><td></td></tr><tr><td>lifecycle</td><td>fk</td><td>Current Lifecycle state of the Agreement</td><td>fk: AgreementLifecycle</td><td></td><td></td><td></td></tr></tbody></table>

### 7.2.3 AgreementData

**Description:** Agreement data contains specifications of exactly what is collected.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>agreement</td><td>string</td><td></td><td>fk: agreement</td><td> </td><td>Uniq</td><td>Y</td></tr><tr><td>name</td><td>fk</td><td>Name of the attribute, for instance, "name" or "age".</td><td></td><td> </td><td> </td><td>Y</td></tr><tr><td>sensitivity</td><td>string</td><td>Categories of sensitivity</td><td></td><td> </td><td> </td><td>Y</td></tr><tr><td>category</td><td>string</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>hash</td><td>string</td><td>In order to sign an Agreement, this relation needs to have a cryptographic hash to be included in the Signature of the Agreement.</td><td></td><td></td><td></td><td></td></tr></tbody></table>

### 7.2.4 Policy

**Description:** A policy governs data and Agreement in the realm of an organisation that is refered to as "data controller"(GDPR) and owner of referencing Agreements.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>name</td><td>string</td><td>Name of the policy.</td><td></td><td> </td><td> </td><td>Y</td></tr><tr><td>version</td><td>string</td><td>Version of the policy.</td><td></td><td> </td><td> </td><td>Y</td></tr><tr><td>url</td><td>string</td><td>Permanent URL at which this very version of the Policy can be read, should not be allowed to change over time.</td><td></td><td></td><td></td><td></td></tr></tbody></table>

### 7.2.5 ConsentRecord

**Description:** A Consent Record expresses consent (as defined in this building block's specification) to a single Agreement. There must be a UNIQUE constraint on (agreement\_revision, individual).

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td>Objects may be passed back by some API endpoints without an id (PK), denoting that they are a "draft", i.e. a ConsentRecord that is not yet stored in the database and only exist in transit. Draft ConsentRecords do not have a Revision, but if paired up with a Signature, a valid Revision should be generated.</td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>agreement</td><td>fk</td><td>The Agreement to which consent has been given.</td><td>fk: Agreement</td><td> </td><td>Uniq</td><td>Y</td></tr><tr><td>agreement_revision</td><td>fk</td><td>The Revision of the agreement to which consent has been given.</td><td>fk: Revision</td><td> </td><td> </td><td>Y</td></tr><tr><td>individual</td><td>fk</td><td>The Individual who has signed this consent record.</td><td>fk: Individual</td><td> </td><td> </td><td>Y</td></tr><tr><td>state</td><td>string</td><td>The state field is used to record state changes after-the-fact. It is maintained by the Consent BB itself. Valid states: unsigned/pending more signatures/signed.</td><td></td><td></td><td></td><td></td></tr><tr><td>signature</td><td>fk</td><td>A signature that hashes all the values of the consent record and has signed with the key of the Individual, making it verifiable and tamper-proof. </td><td>fk: Signature</td><td></td><td></td><td></td></tr></tbody></table>

### 7.2.6 Revision

**Description:** A generic revision model captures the serialized contents of any schema's single row. This is then subject to 1) cryptographic signature and 2) auditing.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>schema</td><td>string</td><td></td><td></td><td> </td><td>Uniq</td><td>Y</td></tr><tr><td>object_id</td><td>string</td><td></td><td></td><td> </td><td> </td><td>Y</td></tr><tr><td>serialized_snapshot</td><td>string</td><td></td><td></td><td> </td><td> </td><td>Y</td></tr><tr><td>timestamp</td><td>string</td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

### 7.2.7 AgreementFilter

**Description:** Query filter for API endpoint listing Agreement objects.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>name</td><td>string</td><td></td><td></td><td> </td><td>Uniq</td><td>Y</td></tr></tbody></table>

### 7.2.8 ConsentRecordFilter

**Description:** Query filter for API endpoint listing ConsentRecord objects.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>opt_in</td><td>boolean</td><td></td><td></td><td> </td><td>Uniq</td><td>Y</td></tr></tbody></table>

### 7.2.9 PolicyFilter

**Description:** Query filter for API endpoint listing Policy objects.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>name</td><td>string</td><td></td><td></td><td> </td><td>Uniq</td><td>Y</td></tr></tbody></table>

### 7.2.10 Controller

**Description:** Details of a data controller.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>name</td><td>string</td><td>Name of data controller (may be omitted if no data is involved).</td><td></td><td> </td><td>Uniq</td><td>Y</td></tr><tr><td>url</td><td>string</td><td>URL of data controller (may be omitted if no data is involved).</td><td></td><td></td><td></td><td></td></tr></tbody></table>

### 7.2.11 Signature

**Description:** A generic signature contains a cryptographic hash of some value, together with a signature created by some private key in another system. Required signing methods: Revision object or another Signature object.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td>Objects may be passed back by some API endpoints without an id (PK), denoting that they are a "draft", i.e. a Signature that is not yet stored in the database and only exists in transit.</td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>payload</td><td>string</td><td>The payload that is signed, is constructed as a serialization of fields verification_method + verification_hash + verification_artifact + verification_signed_by + verification_jws_header. Serialized as a JSON dictionary.</td><td></td><td> </td><td>Uniq</td><td>Y</td></tr><tr><td>signature</td><td>string</td><td>Signature (of payload), the format of the signature should be specified by either verification_method or verification_jws_header.</td><td></td><td></td><td></td><td></td></tr><tr><td>verification_method</td><td>string</td><td>A well-known string denoting which method is used. </td><td></td><td></td><td></td><td></td></tr><tr><td>verification_hash</td><td>string</td><td>Internally generated cryptographic hash of the value to be signed. The hash is (re)produced from the object_type and object_reference - but from the serialized data of those.</td><td></td><td></td><td></td><td></td></tr><tr><td>verification_signed_by</td><td>string</td><td>Because an identifier's information may change over time, there is a need to store that information at the time of signing. In the case of a cryptographic signature, this field should contain some identifier for looking up or verifying the public key of the signing party. In the case of a non-cryptographic signature, this field could contain a natural individual's name, personal number, email address - store a snapshot that binds to the signature at the time of signing. In the case of a cryptographic signature, this may be the fingerprint of the individual's public key or in some cases, a token from the user's ID session.</td><td></td><td></td><td></td><td></td></tr><tr><td>timestamp</td><td>string</td><td>Timestamp of signature, currently this field isn't part of the payload so it's not tamper-proof.</td><td></td><td></td><td></td><td></td></tr></tbody></table>

### 7.2.12 AgreementPurpose

**Description:** Models the purpose of an agreement.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>name</td><td>string</td><td>Name of purpose.</td><td></td><td> </td><td>Uniq</td><td>Y</td></tr><tr><td>description</td><td>string</td><td>Description of purpose.</td><td></td><td></td><td></td><td></td></tr></tbody></table>

### 7.2.13 AgreementLifecycle

**Description:** Models the valid lifecycle states of an Agreement.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>name</td><td>string</td><td>Definition/Preparation/Capture/Use/Proof.</td><td></td><td> </td><td>Uniq</td><td>Y</td></tr></tbody></table>

### 7.2.14 RegistryReference

**Description:** When creating an Individual, we need some input that refers to a functional or foundational ID in an external system.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr></tbody></table>

### 7.2.15 AuditTracker

**Description:** An external tracker receiving information from the system that can be subject to external auditing and verification of correct behaviour. This is one of several notification/monitor/subscription patterns that may be more suitable for an encrypted Pub/Sub service.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr><tr><td>name</td><td>string</td><td>Name of the auditing system.</td><td></td><td> </td><td>Uniq</td><td>Y</td></tr><tr><td>public_key</td><td>string</td><td>The auditing system's public key for encrypting data sent to callback functions.</td><td></td><td></td><td></td><td></td></tr><tr><td>callback_agreement</td><td>string</td><td>A URL receiving a callback with the Agreement object + Revision + AuditEventType.</td><td></td><td></td><td></td><td></td></tr><tr><td>callback_consent_record</td><td>string</td><td>A URL receiving a callback with the ConsentRecord object + Revision + AuditEventType.</td><td></td><td></td><td></td><td></td></tr><tr><td>callback_policy</td><td>string</td><td>A URL receiving a callback with the Policy object + Revision + AuditEventType.</td><td></td><td></td><td></td><td></td></tr></tbody></table>

### 7.2.16 AuditEventType

**Description:** Model for the possible events pertaining to a change to an object subject to auditing. This model is not necessarily a database-backed model, but part of the application code.

**Fields:**

<table data-header-hidden><thead><tr><th></th><th></th><th></th><th></th><th data-hidden></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><strong>Name</strong></td><td><strong>Type</strong></td><td><strong>Description</strong></td><td><strong>Notes</strong></td><td><strong>Foreign Key</strong></td><td><strong>Constraints</strong></td><td><strong>Required</strong></td></tr><tr><td>id</td><td>string</td><td></td><td></td><td> </td><td>PK</td><td>Y</td></tr></tbody></table>
