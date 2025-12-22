# Release Notes

### V1.0

First Publication

### V1.1 (23Q4)

**Section 1.** **Version History**

* **23Q4**: removes 0.1 and 0.5 from version history and indicates potential future releases&#x20;

**Section 2. Description**

Updated ISO **Standards Referenced**

1.0:

* ISO/TS 17975:2015 (older reference)
* ISO/IEC TS 27560 (under development)

**23Q4**:

* ISO/TS 17975:2022 (newer)
* ISO/IEC TS 27560:2023 (newer, finalized)

**Building Block Interactions Table**

**23Q4** removes Digital Registries Building Block for data storage

**Section 6.** **Functional Requirements Wording**

**23Q4**: "It shall be possible to capture and sign all changes to Consent Agreements, Consent Policies and Consent Records in tamper-proof Revisions"

**Design Components Section**

**23Q4** removes:

> "RESTful APIs: All APIs are exposed as RESTful APIs. These are categorised into Organisation APIs, Individual APIs, and Auditing APIs."

**Section 7. Data Structures**

**Data Models Section**

**23Q4**:

* References "fixtures.json" file
* Mentions mock application availability
* Provides GitHub link to mock application
* **ADDs** all references to fixtures.json and mock application

9\. **Internal Workflows Section**

**Title Changes**:

"Consenting at initial registration (Pre-registration) using a centralised ID system" to  "Universal workflow: Recording consent at initial registration (pre-registration)"

**Key Removal**: Version 1.0 specifies "using a centralised ID system" to clarify the ID approach.

**Workflow Names**:

"Consenting after the registration (Post-registration)" to "Universal workflow: Recording consent after the registration (post-registration)"

### V1.2 (23Q4.1)

**API Structure Changes**

**Field Name Updates (snake\_case to camelCase):**

The API specifications changed field naming conventions from snake\_case to camelCase:

**23Q4 (snake\_case):**

* `industry_sector`
* `data_retention_period_days`
* `geographic_restriction`
* `storage_location`
* `external_id`
* `schema_name`
* `object_id`

**23Q4.1 (camelCase):**

* `industrySector`
* `dataRetentionPeriodDays`
* `geographicRestriction`
* `storageLocation`
* `externalId`
* `schemaName`
* `objectId`

2\. **API Response Structure Changes**

**23Q4:** API responses returned objects directly wrapped in response objects

json

```json
{
  "policy": { ... },
  "revision": { ... }
}
```

**23Q4.1:** Some API responses changed to return arrays instead

json

```json
[
  {
    "id": "",
    "name": "",
    ...
  }
]
```

3\. **Data Model Simplifications**

**23Q4.1 removed:**

* Purpose object structure (which had `id`, `name`, `description`, `serialized_hash`)
* Lifecycle object references in Agreement structures
* Some signature verification fields in nested structures

**23Q4.1 simplified:**

* Agreement/ConsentRecord structures are less deeply nested
* Removed circular reference handling in some response examples

4\. **API Endpoint Changes**

**Removed in 23Q4.1:**

* Data Agreement related endpoints (`/config/data-agreement/`, `/service/data-agreement/`)
* Consent Record detailed endpoints
* Webhook configuration endpoints (`/config/webhook/`)
* Several verification endpoints (`/service/verification/`)
* Draft consent record endpoints

**Retained core endpoints:**

* Policy management (`/config/policy/`)
* Individual management (`/service/individual/`)
* Basic audit endpoints (`/audit/consentrecord/`)

**Summary**

Version 23Q4.1 represents a **simplification and standardization effort**, focusing on:

* Consistent camelCase naming throughout APIs
* Reduced complexity in data models
* Streamlined API surface area
* Better alignment with standard REST API conventions

### V1.3.0

**Section 1 - Version History**

* Inclusion of release notes and removal of link to confluence change log that was not maintained
* Update of Authors
* Update of Numbering to semantic versioning

**Section 2 - Description**

* Addition of explanation on GDPR and Public Authorities
* Use of term Data Controller

**Section 3 Terminology**

* Updated to indicate common terminology
* Removal of overlapping terms
* Consistency changes to other ID related BBs
* Move from Table to GovSpecs2.0 heading format

**Section 4 Key Digital Functionalities**

* Use of term Data Controller

**Section 6 Functional Requirements**

* Ensured use of Required/Recommended in requirements in line with GovSpecs2.0



