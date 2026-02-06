# Release Notes

## **Version 1**

***

## _v**1.3.0**_

_Version Date: December 2025_&#x20;

_Authors: Mikael Linden and David Higgins and Ali González-García_

***

### 1. Overview

This release of the Consent Building Block was developed between September and December, 2025 by the Cross-Functional ID Infrastructure Working Group, a super-group of all the key Identity and Trust-related Building Blocks in GovStack (e-signature, identity, Wallet, Consent).&#x20;

Release 1.3 of Consent is the result of a review of all 4 specifications to ensure their are aligned and consistent to a single Identity Universe.

### 2. Changes

#### **Section 1 - Version History**

* Removal of unpublished versions. See [Editorial note](release-notes.md#id-3.-editorial-note)
* Inclusion of release notes and removal of link to confluence change log that was not maintained
* Update of Authors
* Update of Numbering to semantic versioning

#### **Section 2 - Description**

* Addition of explanation on GDPR and Public Authorities
* Use of term Data Controller was added
* The updating of ISO/TS 17975:2015 to ISO/TS 17975:2022 definition of concern on the body (missed on version 1.1.0, where this update was introduced) gave change to a more contextualized definition of concern for which amendments were introduced.
* Assumptions section was renamed "Out-of-scope Assumptions" and placed second-to-last. The reasoning for this is that before it stated it was about pre-conditions, but only the first bullet regarding Data Disclosure Agreements constituted a pre-condition. The rest of them were simply elements outside the scope of the specification. An "Out-of-scope Assumptions" section is also available on other specifications, so the change improves consistency.

#### **Section 3 Terminology**

* Updated to indicate common terminology
* Removal of the entry for `Legal Entity`, as it overlaps to the entries `Data Provider`, `Consumer`, and `Processing Auditor`.&#x20;
* Consistency changes to other ID related BBs
* Move from Table to [GovSpecs 2.0](https://govstack.global/news/govspecs-2-0-strategy-2025-2027-a-blueprint-for-future-ready-digital-public-services/) heading format

#### **Section 4 Key Digital Functionalities**

* Use of term Data Controller was added
* Updated table structure for Use-cases so that now Operation and Functionality are visible
* Corrected the Use-cases links to use the version corresponding to the current specification (it was previously linked to the ones on version 1.0). Whenever the use-case operation was not available, removed the link and noted the unavailability so readers are not directed to non-existent content.

#### **Section 6 Functional Requirements**

* Ensured use of Required/Recommended in requirements in line with [GovSpecs 2.0 strategy](https://govstack.global/news/govspecs-2-0-strategy-2025-2027-a-blueprint-for-future-ready-digital-public-services/).

#### **Use-cases**

* Added a "For consideration of Future Log" notice to UC-C-PIC-A-003, UC-C-PIC-A-004 and UC-C-PIC-A-005 as they were empty.
* Removed the content of UC-C-PIC-I-004: Consent agreement change notification as it was an exact copy of UC-C-PIC-I-003: Withdraw or update existing consent and placed a "For consideration of Future Log" notice&#x20;

### 3. Editorial note

_Author: Ali González-García_

Release 1.3 reworks the previous versioning system from [CalVer](https://calver.org/) to [Semver](https://semver.org/) as a strategic decision that follows [GovStack's 2.0 strategy](https://govstack.global/news/govspecs-2-0-strategy-2025-2027-a-blueprint-for-future-ready-digital-public-services/), as well as a revamped Version History section that includes key version information, such as publication dates and richer comments.

It removes from the version history page all unpublished versions, because they denote internal GovStack revision and processes and cannot be consulted as standalone versions themselves. On future versions, this metadata will be published as part of the documentation of the GovStack project that belongs to the specification publishing which will include richer information such as working group composition, meetings and key decision information.

The current release notes section is also an addition to this batch. The purpose is to provide implementers with a quick and clear reference of changes and additions between versions, among with context as to why the GovStack community has decided to publish the release.&#x20;

The Terminology section now uses Heading tags for definitions instead of a table. This adds semanticity to each definition and makes it linkable, as each definition is provided with an HTML `id` attribute.

We hope the provided changes make for a better legibility experience of this specification.

***

## _v1.2 (known as 23Q4.1)_

### **1. Overview**

Version 1.2 represents a **simplification and standardization effort**, focusing on:

* Consistent camelCase naming throughout APIs
* Reduced complexity in data models
* Streamlined API surface area
* Better alignment with standard REST API conventions

### **2. Changes**

#### 2.1 Field Name Updates (snake\_case to camelCase):

The API specifications changed field naming conventions from snake\_case to camelCase:

<table data-full-width="false"><thead><tr><th>23Q4 (snake_case)</th><th>23Q4.1 (camelCase)</th></tr></thead><tbody><tr><td><code>industry_sector</code></td><td><code>industrySector</code></td></tr><tr><td><code>data_retention_period_days</code></td><td><code>dataRetentionPeriodDays</code></td></tr><tr><td><code>geographic_restriction</code></td><td><code>geographicRestriction</code></td></tr><tr><td><code>storage_location</code></td><td><code>storageLocation</code></td></tr><tr><td><code>external_id</code></td><td><code>externalId</code></td></tr><tr><td><code>schema_name</code></td><td><code>schemaName</code></td></tr><tr><td><code>object_id</code></td><td><code>objectId</code></td></tr></tbody></table>

#### 2.2 API Response Structure Changes

**Version 1.1:** API responses returned objects directly wrapped in response objects

{% code title="response_v1-1.json" %}
```json
{
  "policy": { ... },
  "revision": { ... }
}
```
{% endcode %}

**Version 1.2:** Some API responses changed to return arrays instead

{% code title="response_v1-2.json" %}
```json
[
  {
    "id": "",
    "name": "",
    ...
  }
]
```
{% endcode %}

#### 2.3 Data Model Simplifications

**Removed:**

* Purpose object structure (which had `id`, `name`, `description`, `serialized_hash`)
* Lifecycle object references in Agreement structures
* Some signature verification fields in nested structures

**Simplified:**

* Agreement/ConsentRecord structures are less deeply nested
* Removed circular reference handling in some response examples

#### 2.4 API Endpoint Changes

**Removed:**

* Data Agreement related endpoints (`/config/data-agreement/`, `/service/data-agreement/`)
* Consent Record detailed endpoints
* Webhook configuration endpoints (`/config/webhook/`)
* Several verification endpoints (`/service/verification/`)
* Draft consent record endpoints

**Retained core endpoints:**

* Policy management (`/config/policy/`)
* Individual management (`/service/individual/`)
* Basic audit endpoints (`/audit/consentrecord/`)



***

## _v1.1 (known as 23Q4)_

### **1. Changes**

#### Section 1. Version History

* Removed v0.1 and v0.5 from version history and indicates potential future releases&#x20;

#### Section 2. Description

Updated ISO **Standards Referenced**

| Version 1.0                          | Version 1.1 (known as 23Q4)              |
| ------------------------------------ | ---------------------------------------- |
| ISO/TS 17975:2015 (older reference)  | ISO/TS 17975:2022 (newer)                |
| ISO/IEC TS 27560 (under development) | ISO/IEC TS 27560:2023 (newer, finalized) |

**Building Block Interactions Table**

Removed [Digital Registries Building Block](https://registries.govstack.global/) for data storage.

#### **Section 6.** **Functional Requirements Wording**

**Added**: "It shall be possible to capture and sign all changes to Consent Agreements, Consent Policies and Consent Records in tamper-proof Revisions"

**Removed**:

From Design Components section

> "RESTful APIs: All APIs are exposed as RESTful APIs. These are categorised into Organisation APIs, Individual APIs, and Auditing APIs."

#### Section 7. Data Structures

**Added section:**

**7.3 Example data and mock application**

* References "fixtures.json" file
* Mentions mock application availability
* Provides GitHub link to mock application
* **ADDs** all references to fixtures.json and mock application

#### 9. Internal Workflows Section

**Title Changes**:

"Consenting at initial registration (Pre-registration) using a centralised ID system" to  "Universal workflow: Recording consent at initial registration (pre-registration)"

**Key Removal**: Version 1.0 specifies "using a centralised ID system" to clarify the ID approach.

**Workflow Names**:

"Consenting after the registration (Post-registration)" to "Universal workflow: Recording consent after the registration (post-registration)"



***

## _v1.0_

First Publication





