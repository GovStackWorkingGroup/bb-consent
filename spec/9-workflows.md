---
description: >-
  This section provides a detailed view of how this Building Block will interact
  with other Building Blocks to support common use cases.
---

# 9 Internal Workflows

This section lists workflows that this Building Block must support. Other workflows may be implemented in addition to those listed.

## 9.1 About universal workflows

The Workflow Building Block triggers the need for consent as part of the general business flow. The assumption is that a consenting process never exists outside of a purposeful comprehensive business process. Hence, it is important to define and control the data processing activities as part of a holistic data service.

This section lays out key universal consent workflows that can be re-used within the various use cases ([see Workflow Building Block](https://govstack.gitbook.io/bb-workflow/v/workflow-1.0/)). This enforces the best practices for organisations to adhere to personal data processing standards in any given context and jurisdiction. In these sequences, we have removed the Digital Registries Building Block in the sequence for simplicity. It will store all persistent consent data.

## 9.2 Universal workflow: Recording consent at initial registration (pre-registration)

The first and somewhat unique use case is related to the need for consent when the Individual is not yet provisioned in the System processing the data. In such cases, the workflow requires the creation of a valid and trusted Foundational ID to be linked with the Consent Record. Below is shown how a pre-registration use of Consent's Workflow works.

### 9.2.1 Internal workflow

* At the very beginning, the registration process will know which `Agreement` IDs are eligible for registration and fetch the `Agreement`(s) and their related objects, such as `AgreementPurpose`, `AgreementData`, `Controller` and `Policy`.
* The signing process is initiated by calling the API endpoint `/service/individual/record/consentrecord/draft/` which produces two resulting instances: `ConsentRecord`, `Signature`. None of these are stored in the database, so they have no `id` value supplied. They will be used after the registration process is completed.
* Once the registration is completed, and a functional or foundational ID (which ever is desired to use, the Consent BB uses the notion of "external ID" here) is known by the Identity BB, the registration process should resolve if this ID has previously been used to store consent by a request to `/service/individuals/`. If an `Individual` object does not exist, a call is issued to `/service/individual/` to create the individual in the Consent BB with a reference used by the Identity Building Block.
* At the end of the registration, the API endpoint `/service/individual/record/consentrecord/` is called with the draft `ConsentRecord` and `Signature` objects to be saved.

#### Signing the draft `ConsentRecord`

When a draft is created, the Consent BB should issue a pair of object instances that are not saved in the database. They have the same schema as the real database objects, but the `id` field is left blank.

The Signature object would normally contain the content of a Revision object in its `payload` field. In this case, it will contain the content of a Revision object that was not stored in the database when it was generated, so it doesn't have an ID yet.

We use the two boolean flags `Revision.signed_without_object_id` and `Signature.signed_without_object_reference` to denote that the Revision and Signature objects were hashed and signed without any reference to a database row. However, these fields are filled in later! When Signature and Revision objects are validated by serializing and hashing the data that they claim to represent, we need to note these two flags so we don't generate the wrong hashes or compare serialized values wrongly.

#### **Edge cases**

* `Agreement` and `Policy` objects are revisioned and if the registration process wishes to initiate a different revision from the latest active revision, it should be equipped with the knowledge of the revision IDs.
* In cases where a valid `ConsentRecord` and `Signature` pair already exists in the system, those should be returned instead, and the client-side can understand from the timestamp of the object that it has been created at a previous occasion. This can be resolved by calling `/service/individual/record/agreement/{agreementId}/`.
* If the latest active `Agreement` or `Policy` revisions change, then those changes have to be detected when fetching related objects. The expected `Revision` ID is added to calls that fetch related objects and APIs should fail if there is a mismatch and a different set of related objects are returned compared to the latest active Agreement.
* **CONSENT CAN BE OMITTED BY THE USER**. The Consent BB does not know about this unless informed, since the Application is responsible for the UI. If there is a need to record an opt-out, this is possible to do with the same process, but simply marking the `ConsentRecord` as an explicit opt-out. The Registration process may also skip recording the opt-out and proceed to an alternative path.

#### Sequence diagram

```mermaid  fullWidth="true"
sequenceDiagram

actor Individual

Individual->>+Application: Initiates registration process
Application->>+Consent BB: For each known Agreement ID,<br>Fetches the active revisions of Agreement(s)
Consent BB-->>+Application: Agreement(s) and Revisions(s) objects
note right of Consent BB: Future RBAC will be imposed<br>through HTTP layer headers<br>to limit application access
Application->>+Consent BB: Fetches related objects:<br>Policy, AgreementPurpose(s), AgreementData(s)
Consent BB-->>+Application: Related objects:<br>Policy, AgreementPurpose(s), AgreementData(s)
Application-->Application: Obtains registration data and<br>displays consent information according to<br>Consent BB UX guidelines
Application->>Consent BB: Fetches Draft ConsentRecord and Signature objects
Consent BB-->>Application: ConsentRecord, Signature
Application-->Application: Registers an individual through Identity BB<br>Foundational or Functional ID is know.
Application-->Application: Obtains digital signatures from Identity BB (calling eSignature BB)<br>Adds signature to Signature object
Application->>Consent BB: Check if Individual with Foundational/Functional ID<br>exists (using RegistryReference)
Consent BB-->>Application: Existing Individual object or None
Application->>Consent BB: Create Individual if None exists
alt A unique Individual object was submitted
Consent BB-->>Application: Individual
else
Consent BB-->>Application: Failure - Individual already exists
end
Application->>Consent BB: Submit final ConsentRecord and<br>Signature objects with Individual ID added
Consent BB->>Consent BB: Validates that Signature's payload matches<br>expected serialization of ConsentRecord object
Consent BB->>Atomic DB transaction: Initiate transaction
Consent BB->>Atomic DB transaction: Creates ConsentRecord object<br>from draft
Consent BB->>Atomic DB transaction: Creates Revision of<br>serialized ConsentRecord.
note right of Atomic DB transaction: The payload that was signed<br>MUST be the exact content of<br>the Revision's serialized_snapshot 
Consent BB->>Atomic DB transaction: Creates Signature from<br>draft.
Atomic DB transaction-->>Consent BB: Success
Consent BB->>Atomic DB transaction: Commit transaction
Consent BB-->>Application: ConsentRecord, Revision
Consent BB->>PubSub: Signal new ConsentRecord
note over PubSub: All PubSub interactions<br>are pending a future<br>Consent BB release
note right of Individual: Consent can now be<br>assumed valid, and<br>the registration process can conclude. 
```

### 9.2.2 Building block interactions

```mermaid  fullWidth="true"

sequenceDiagram

actor Individual
Individual->>+Application: Invoke registration workflow
Application->>+Workflow BB: Trigger registration workflow

note over Workflow BB: Identifies the need for consent

Workflow BB->>+Consent BB: Fetch consent agreement (Registration)
Consent BB-->>-Workflow BB: Returns consent agreement
Workflow BB-->>-Application: Returns consent agreement
Application-->>-Individual: Show consent agreement to fetch data 

note over Individual: The individual agrees<br />to the consent agreement 

Individual->>+Application: Accept consent agreement
Application->>+Foundational ID: Redirect to Foundational ID UI

Foundational ID-->>-Individual: Return Foundational ID authentication UI
Individual->>+Foundational ID: Provide credentials to perform authentication
Foundational ID-->>-Application: Return Foundational ID token (e.g. JWT token) 

note over Application: Foundational ID token recieved<br />is the proof of consent

Application->>+Workflow BB: Fetch data workflow
note right of Workflow BB: Fetch data, <br />For e.g. a population regsitry.

Workflow BB-->>-Application: Confirms the workflow
Application-->>+Workflow BB: Record consent against consent agreement (Foundation ID token, Appl user ID)
Workflow BB-->>+Consent BB: Record consent against the consent agreement
Consent BB-->>-Workflow BB: Return consent ID
Workflow BB-->>-Application: Return consent ID
Application-->>-Individual: Confirm registration

note over Foundational ID: Individual is registered
```

## 9.3 Universal workflow: Recording consent after the registration (post-registration)

In more frequent situations, when the individual is already provisioned in the System (post-registration), the consent workflow uses the existing ID tokens, and only the `ConsentRecord` is to be created.

### 9.3.1 Internal workflow

* As with the [Registration Workflow](9-workflows.md#9.2-universal-workflow-recording-consent-at-initial-registration-pre-registration), the Application needs to know IDs of `Agreement` objects that are eligible for the consent beforehand. It may optionally use a `Revision` ID for an Agreement to specify a specific version of the `Agreement`. Essentially, the application developer should embed these IDs in the process as predefined data.
* In this workflow, the Application has authenticated the individual (user), and if the user consents to the presented Agreement, the `ConsentRecord` will be stored with a relation to an `Individual` entity in the Consent BB. The `Individual` schema has a number of optional fields that will relate it to the original user's identity in a _desired manner_. In other words, the identity of the user is exposed to the Consent BB in a _desired manner_. There are several options:
  * The individual can be managed through a Foundational ID, Functional ID which can be useful for the Consent BB to allow the user to manage all their `ConsentRecord`s at a later stage.
  * A session-related ID that the application or other data consumers can otherwise use at a later stage.
  * An obscurified ID that can be resolved through the Identity BB such that all `ConsentRecord` management can only be performed with a relation to the real individual through authorization of the Identity BB.
* No matter which `Individual` ID is used, the Application is responsible for either fetching an existing or creating a new `Individual` object in the Consent BB.
* The Application is responsible for presenting the UI and calls the necessary endpoints of the Consent BB to store the `ConsentRecord`.
* A draft `ConsentRecord` and `Signature` object is handed to the Application, which it should finalize and submit back.
* There are several options for finalizing the draft `Signature` object: The individual may be requested to explicitly sign the consent through Identity BB and eSignature BB. However, another trusted signing party may also be eligible to record and sign the validity of the ConsentRecord object.

#### Edge cases

* The Application may want to check if consent has already been obtained! This can be done at several stages, if there is a need to guard against parallel processes.
* A `ConsentRecord` may be created at first, but if the signing process fails and no `Signature` object is created, the Application should perform due diligence and delete the `ConsentRecord`.
* Consent can always be omitted during the process or at any later stage. The Application needs to provide an alternative path. This can for instance be handled with the Workflow BB.

#### Sequence diagram

```mermaid  fullWidth="true"
sequenceDiagram

actor Individual
Individual->>+Application: Invokes a consent process

Application->>+Consent BB: For each known Agreement ID,<br>Fetches the active revisions of Agreement(s)
Consent BB-->>+Application: Agreement(s) and Revisions(s) objects
note right of Consent BB: Future RBAC will be imposed<br>through HTTP layer headers<br>to limit application access
Application->>+Consent BB: Fetches related objects:<br>Policy, AgreementPurpose(s), AgreementData(s)
Consent BB-->>+Application: Related objects:<br>Policy, AgreementPurpose(s), AgreementData(s)
Application-->Application: Obtains registration data and<br>displays consent information according to<br>Consent BB UX guidelines
Application->>Consent BB: Check if Individual with<br>Foundational/Functional ID/other ID<br>exists
Consent BB-->>Application: Existing Individual object or None
Application->>Consent BB: Create Individual if None exists
alt A unique Individual object was submitted
Consent BB-->>Application: Individual
else
Consent BB-->>Application: Failure - Individual already exists
end
Application->>Consent BB: Fetches Draft ConsentRecord and Signature objects
Consent BB-->>Application: ConsentRecord, Signature
Application->>Application: Obtain valid signature<br>through desired signature method<br>(for instance Identity BB and eSignature BB)
Application->>Consent BB: Submit final ConsentRecord and<br>Signature objects with Individual ID added
Consent BB->>Consent BB: Validates that Signature's payload matches<br>expected serialization of ConsentRecord object
Consent BB->>Atomic DB transaction: Initiate transaction
Consent BB->>Atomic DB transaction: Creates ConsentRecord object<br>from draft
Consent BB->>Atomic DB transaction: Creates Revision of<br>serialized ConsentRecord.
note right of Atomic DB transaction: The payload that was signed<br>MUST be the exact content of<br>the Revision's serialized_snapshot 
Consent BB->>Atomic DB transaction: Creates Signature from<br>draft.
Atomic DB transaction-->>Consent BB: Success
Consent BB->>Atomic DB transaction: Commit transaction
Consent BB-->>Application: ConsentRecord, Revision
Consent BB->>PubSub: Signal new ConsentRecord
note over PubSub: All PubSub interactions<br>are pending a future<br>Consent BB release
note right of Individual: Consent can now be<br>assumed valid

```

### 9.3.2 Building block interactions

```mermaid  fullWidth="true"

sequenceDiagram

actor Individual

note over Individual: The individual is signed in<br />to the application

Individual->>+Application: Invoke a consent agreement workflow
Application->>+Workflow BB: Triggers the consent agreement workflow

Workflow BB->>+Consent BB: Fetch consent agreement
Consent BB-->>-Workflow BB: Returns consent agreement
Workflow BB-->>-Application: Returns consent agreement
Application-->>-Individual: Shows consent agreement

note over Individual: The individual agrees/disagrees<br />to the consent agreement 

Individual->>+Application: Accepts/Rejects the consent agreement
Application-->>+Workflow BB: Records consent against the consent agreement (Foundation ID token, Application user ID)
Workflow BB-->>+Consent BB: Records consent against the consent agreement (Foundation ID token, Application user ID)
Consent BB-->>-Workflow BB: Returns consent ID
Workflow BB-->>-Application: Returns consent ID

Application-->>-Individual: Accepts/Rejects the consent agreement
```

## 9.4: Universal workflow: Consent Verification

In this universal workflow, we check if a valid `ConsentRecord` exists or not for a given data processing event within a business process. This may be the immediate continuation of a consenting workflow by the same System that acquired the `ConsentRecord` or it may be used by a separate business process by a different Application or at a different moment in time. The same verification workflow may be also used for auditing purposes.

### 9.4.1 Internal workflow

* In order to query for the existence of a `ConsentRecord`, the Application needs to know about an `Individual` and an `Agreement`.
* The `Individual` can be resolved through a query using the `RegistryReference` schema as a parameter. The Consent BB will then return matching `Individual` objects.
* As is seen in other workflows, the `Agreement` is resolved by preexisting knowledge of the `Agreement` ID, and the Application may further use a specific `Revision` ID of the Agreement or ask for the latest active `Agreement` by _not_ specifying a `Revision`.
* By using the Individual and `Agreement` IDs, it is possible for the Application to fetch the latest active `ConsentRecord` and `Signature` to resolve the state of consent.
*

### Sequence diagram

TODO

### 9.4.2: Building block interactions

```mermaid  fullWidth="true"
sequenceDiagram

Application->>+Workflow BB: Triggers the consent verification workflow (consent agreement ID)
note over Application: The Application is in the workflow<br />of processing personal data that<br />requires consent. 

Workflow BB->>+Consent BB: Fetch consent ID (consent agreement ID, user ID)
Consent BB-->>-Workflow BB: Returns consent record
Workflow BB-->>-Application: Returns consent record

note over Application: Application checks if the consent exists<br />and processes the data based on it
```
