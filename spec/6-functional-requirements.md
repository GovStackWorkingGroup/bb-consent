---
description: This section lists the technical capabilities of this Building Block.
---

# 6 Functional Requirements

The functional requirements section lists the technical capabilities that this Building Block should have. These requirements should be sufficient to deliver all functionality that is listed in the Key Digital Functionalities section. These functional requirements do not define specific APIs, they provide a list of information about functionality that must be implemented within the Building Block. These requirements should be defined by subject-matter experts and don’t have to be highly technical in this section.

## 6.1 Administrator User Functionalities

Agreement Configuration Requirements.

* It shall be possible to create a consent agreement, either based on an existing or new data policy template. Each consent agreement shall be under version control (REQUIRED)
* It shall be possible to view an existing consent agreement (REQUIRED)
* It shall be possible to update an existing consent agreement (REQUIRED)
* It shall be possible to terminate an existing consent agreement (REQUIRED)
* It shall be possible to capture and sign all changes to Consent Agreements, Consent Policies and Consent Records in tamper-proof Revisions (REQUIRED)
* It shall be possible to subscribe to enable or disable a change notification towards users (REQUIRED)
* It shall be possible to trigger a change notification when there are changes done to an existing consent agreement (RECOMMENDED)
* The Building Block shall log all administrative functions (REQUIRED)

## 6.2 Individual User Functionalities

* It shall be possible to view the associated consent agreement if it exists (REQUIRED)
* It shall be possible to agree or opt-in or sign a consent agreement (REQUIRED)
* It shall be possible to opt-out of a previously signed or agreed consent agreement (REQUIRED)
* All individual consent actions shall be logged (REQUIRED)
* It shall be possible to enable or disable consent change notification (REQUIRED)
* It shall be possible to trigger a consent agreement change notification towards individuals (RECOMMENDED)

## 6.3 Data Processing Auditor User Functionalities

* All consent logs shall be tamperproof, Audit logging (REQUIRED)
* It shall be possible to view and verify a shared consent agreement (REQUIRED)
* It shall be possible to view and verify a shared consent agreement (REQUIRED)
* It shall be possible to filter and sort all objects’ revision histories can be filtered and sorted (REQUIRED)

## Design and Components of Consent Building Block

Within the scope of Consent Building Block version 1.0, the required components are as given. &#x20;

<figure><img src="images/consent-bb-components.png" alt=""><figcaption><p><a href="https://app.moqups.com/P01asyy7ba/view/page/aeb6c8723">Diagram Source</a></p></figcaption></figure>

**Consent Agreement Configuration Handler:** handles the creation, updation & deletion of consent agreements for organisations. Organisations can be Data Providers or Data Consumers.

**Consent Record Handler:** enables Individuals to view data usage and consent record.

**Notification Handler:** handles all notification configurations and notifications requested by different subscribers.

**Administrative User Interface and Client Software Development Kit:** these are readily available components that can configure and use the services offered, making integration easy and low code.
