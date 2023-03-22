---
description: This section lists the technical capabilities of this Building Block.
---

# 6 Functional Requirements

The functional requirements section lists the technical capabilities that this Building Block should have. These requirements should be sufficient to deliver all functionality that is listed in the Key Digital Functionalities section. These functional requirements do not define specific APIs - they provide a list of information about functionality that must be implemented within the Building Block. These requirements should be defined by subject-matter experts and don’t have to be highly technical in this section.

## 6.1 Consent Agreement Configuration Requirements

| **Name**                         | **Description**                                                                                                                                                     | **Optionality** |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Create Consent Agreement         | It shall be possible to create a consent agreement, either based on an existing or new data policy template. Each consent agreement shall be under version control. | MUST            |
| View Consent Agreement           | It shall be possible to view an existing consent agreement.                                                                                                         | MUST            |
| Update Consent Agreement         | It shall be possible to update an existing consent agreement.                                                                                                       | MUST            |
| Terminate Consent Agreement      | It shall be possible to terminate an existing consent agreement.                                                                                                    | MUST            |
| Revision history                 | It shall be possible to capture and sign all changes to Consent Agreements, Consent Policies and Consent Records in tamper-proof Revisions.                         | MUST            |
| Change notification subscription | It shall be possible to subscribe to enable or disable a change notification towards users.                                                                         | MUST            |
| Change notification              | It shall be possible to trigger a change notification when there are changes done to an existing consent agreement.                                                 | MAY             |
| Logging                          | The Building Block shall log all administrative functions.                                                                                                          | MUST            |

## 6.2 Individual Consent Requirements

| **Name**                         | **Description**                                                                              | **Optionality** |
| -------------------------------- | -------------------------------------------------------------------------------------------- | --------------- |
| View consent agreement           | It shall be possible to view the associated consent agreement if it exists.                  | MUST            |
| Agree (Opt-in)                   | It shall be possible to agree or opt-in or sign a consent agreement.                         | MUST            |
| Withdraw (Opt-out)               | It shall be possible to opt-out of a previously signed or agreed consent agreement.          | MUST            |
| Logging                          | All individual consent actions shall be logged.                                              | MUST            |
| Change notification subscription | It shall be possible to enable or disable consent change notification.                       | MUST            |
| Change notification              | It shall be possible to trigger a consent agreement change notification towards individuals. | MAY             |

## 6.3 Consent Audit Requirements

| **Name**                              | **Description**                                                                                     | **Optionality** |
| ------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------- |
| Audit logging                         | All consent logs shall be tamperproof.                                                              | MUST            |
| View and verify the consent agreement | It shall be possible to view and verify a shared consent agreement.                                 | MUST            |
| View and verify consents              | It shall be possible to view and verify a signed consent agreement.                                 | MUST            |
| Revision list                         | It shall be possible to filter and sort all objects’ revision histories can be filtered and sorted. | MUST            |
