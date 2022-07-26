# 4 Key Digital Functionalities

Consent BB enables the organisations to enforce Data Policies that require signed consent by Individuals for the use of their personal data. Its key purpose is to allow individuals to view Consent Agreements and sign or withdraw their consent on what personal data is used and accessible to organisations. It also clarifies the Data Policy applied, such as the purpose, retention period, jurisdiction, third-party data sharing, etc.

The Consent BB implements the key functionalities described in the [consent management lifecycle](./2-description.md#23-consent-agreement-lifecycle). It includes the ability to configure consent agreement by an organisation admin, present consent requests towards individuals, capture consents, enable queries if consent exists or not, and enable independent audit of consents. 
## 4.1 Assumptions

This lays out the pre-conditions needed for anyone to use Consent BB.

1. Data Disclosure Agreements between organisations are already in place. For e.g. a healthcare organisation has already got the required authorisation to use the citizen data registry.
2. To link a Consent Agreement with the specific Individual, Consent BB assumes the authentication & authorization to be handled in a trusted manner outside of it (see below).
3. Within the early scope of the Consent BB, the act of delegating is kept outside the scope of Consent BB. It is assumed that the authorisation to act on behalf of someone else is already resolved.
4. It is the organisation's (a Data Provider or a Data Consumer) obligation to manage and implement internal policies towards its employees relating to their individual responsibilities for Personal data processing integrity, specifying it in the employment contract or by other means.
## 4.2	Consent BB Components

Within **the scope of Consent BB version 1.0,** the required components are as given:
![alt_text](images/consent-bb-components.png "image_tooltip")
[Diagram Source](https://app.moqups.com/P01asyy7ba/view/page/ad64222d5)

**Consent Agreement Configuration Handler** - handles the creation, updation & deletion of consent agreements for organisations. Organisations can be Data Providers or Data Consumers

**Consent Record Handler ** "enables Individuals to view data usage and consent record.

**Notification Handler: ** Handles all notification configurations and notifications requested by different subscribers.

**Administrative UI and client UI SDKs**: These are readily available components that can configure and use the services offered, making integration easy and low code.

**RESTful APIs**: All APIs are exposed as RESTful APIs. These are categorised into Organisation APIs, Individual APIs and Auditing APIs.
## 4.3 Interactions with other Building Blocks

The overall relationship diagram is shown below.

![alt_text](images/consent-bb-relationships.png "image_tooltip")

[Diagram Source](https://drive.google.com/file/d/1Kfyja3C-QA5spi20p7Bu8kz80bVkJ5i7/view?usp=sharing)

The table below summarises the key relationships consumed during a consent transaction.

| Building block          | Relationship description                                                                                                                         |
| :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| Identity BB             | It is assumed the Consent BB has already obtained requisite access tokens                                                                        |
| Digital Registries BB   | This is used to store any consent agreement, individual consent receipts etc.                                                                    |
| Workflow BB             | Manages the workflow and rules associated with requiring or not requiring consent to use personal data.                                          |
| Scheduler  BB           | Provides an engine for time-based triggers to various events of an automated business process, which might also require consent.                 |
| Information mediator BB | The information mediator BB provides a gateway for exchanging data related to consenting workflows; it also provides logs for auditing purposes. |

## 4.4	Functionalities 

The functionalities are derived from the [consent agreement lifecycle](./2-description.md#23-consent-agreement-lifecycle) and categorised according to the [Actors](./2-description.md#24-actors) described above. While the consenting workflows (as described above) are implicitly considered the centrepiece of Consent BB, it is important to realise that the integrity of consent management can only be achieved if robust configuration before and auditing after the Consent Agreement signing and Consent Record verification activities are in place. Hence, the functionalities are described following the logical sequence of the consent agreement lifecycle and they are all equally important components of the Consent BB.  

The consent process (creating and signing Consent Agreements and Consent Records) is initially managed in the application provided by the Organisation that is legally required to collect the consent. Since it can be either a Data Consuming organisation or a Data Providing organisation, the Consent BB allows both to be able to verify their conformance with the underlying Data Policy, both organisations must be able to access and use the application.

While the Actors generally fall in line with the categories of the functionalities, it is important to realise that “auditing” functions in the narrow sense - verifying if data processing is being (or has been) processed according to the Data Policy requiring a consent - is relevant to various entities involved in the data processing. For this reason, the generic “verification” activity may be executed as part of various workflows satisfying the needs of different actors. 

### 4.4.1	Administrator User Functionalities

The table below summarises the key use cases identified for an organisation's Administrator. Organisations can be Data Consumers or Data Providers, i.e. the organisations legally delegated the responsibility for collecting consent for the systems handling personal data processing. 

It is foreseen that one organisation involved in the data processing transaction takes responsibility for the configuration of Data Policy and respective Consent Agreements(s), and so the organisation’s Administrator maintains the required configurations.

<table>
  <tr>
   <td><strong>Consent management use-cases</strong>
   </td>
   <td><strong>Link(s) to the UCS</strong>
   </td>
  </tr>
  <tr>
   <td>CREATE CONSENT AGREEMENT -  Here, an organisation Administrator creates a Consent Agreement based on the Data Policy requirements.
   </td>
   <td><a href="https://docs.google.com/document/d/1kIyZrfRkM6NC40S7QYGrmX9HpJI3P0y5beYiGNMAk9Q/edit#bookmark=id.fh1b0ry1h3gd">UC-C-PIC-A-001</a>
   </td>
  </tr>
  <tr>
   <td>UPDATE CONSENT AGREEMENT - Here, an organisation Administrator updates the Consent Agreement based on the Data Policy requirements..
   </td>
   <td><a href="https://docs.google.com/document/d/1kIyZrfRkM6NC40S7QYGrmX9HpJI3P0y5beYiGNMAk9Q/edit#heading=h.9l9ar3fqqo6u">UC-C-PIC-A-002</a>
   </td>
  </tr>
  <tr>
   <td>READ CONSENT AGREEMENT - Here, an organisation Administrator reads the Consent Agreement.
   </td>
   <td><a href="https://docs.google.com/document/d/1kIyZrfRkM6NC40S7QYGrmX9HpJI3P0y5beYiGNMAk9Q/edit#bookmark=id.fh1b0ry1h3gd">UC-C-PIC-A-003</a>
   </td>
  </tr>
  <tr>
   <td>DELETE CONSENT AGREEMENT - a special case of consent agreement update
   </td>
   <td><a href="https://docs.google.com/document/d/1kIyZrfRkM6NC40S7QYGrmX9HpJI3P0y5beYiGNMAk9Q/edit#bookmark=id.fh1b0ry1h3gd">UC-C-PIC-A-004</a>
   </td>
  </tr>
  <tr>
   <td>CONSENT AGREEMENT CHANGE NOTIFICATION - Notifications for Data Providing and Data Consuming Systems, as well as Individuals upon changes to Agreement or Policy configuration.
   </td>
   <td><a href="https://docs.google.com/document/d/1kIyZrfRkM6NC40S7QYGrmX9HpJI3P0y5beYiGNMAk9Q/edit#bookmark=kix.is6kbi5y5d7c">UC-C-PIC-A-005</a>
   </td>
  </tr>
</table>

### 4.4.2	Individual User Functionalities

The table below summarises the key use cases identified for the Individuals. 

<table>
  <tr>
   <td><strong>Consent management use-cases</strong>
   </td>
   <td><strong>Link to the UCS</strong>
   </td>
  </tr>
  <tr>
   <td>VIEW CONSENT - Here, the Individual views the Consent Agreement and the conditions for personal data processing (with adequate clarity for informed understanding).  This includes obtaining copies of the consent agreement.
   </td>
   <td><a href="https://docs.google.com/document/d/1FLm2fkKp5uU_2lsI4xDoRP1U8rgqrNLqOQhrO6xpYmY/edit?usp=sharing">UC-C-PIC-I-001</a>
   </td>
  </tr>
  <tr>
   <td>GIVE CONSENT - Here, the Individual signs a Consent Agreement during a data sharing workflow. Note that this can also happen offline without data sharing in place. 
   </td>
   <td><a href="https://docs.google.com/document/d/1kdk8iaH2khX3gZ3_0fevi510JWIL4hRWOr8Tjun6x6k/edit?usp=sharing">UC-C-PIC-I-002</a>
   </td>
  </tr>
  <tr>
   <td>WITHDRAW CONSENT - Or update existing consent
   </td>
   <td><a href="https://docs.google.com/document/d/1FLm2fkKp5uU_2lsI4xDoRP1U8rgqrNLqOQhrO6xpYmY/edit?usp=sharing">UC-C-PIC-I-003</a>
   </td>
  </tr>
  <tr>
   <td>Consent agreement change notification
   </td>
   <td><a href="https://docs.google.com/document/d/1FLm2fkKp5uU_2lsI4xDoRP1U8rgqrNLqOQhrO6xpYmY/edit?usp=sharing">UC-C-PIC-I-004</a>
   </td>
  </tr>
</table>

### 4.4.3	Data Processing Auditor User Functionalities

The table below summarises the key use cases identified for the Data Processing Auditor.

**Important note**: In the Consent BB, we define the Data Processing Auditor's role (see 1.3 Terminology and 1.5.3 Actor definition)  as an organisation's auditor implementing the Consent BB. The auditor role will most probably be akin to a Data Protection Officer (DPO), possibly from an external third party organisation and involve activities outside of the Consent BB. 

To avoid ambiguity, we use the precise term Data Processing Auditor to stress the specificity of tasks to be performed by and for the Consent BB; all other actions not within the Consent BB's scope are considered as an external prerequisite and as a “black box” activity. With respect to audit, this role is distinguished from the data policy auditor.

**Also to consider:** “READ CONSENT STATUS” use-case is also used by any workflow (and Actor) that requires verification of the consent status (for example, before executing the data transfer from Data Providing System to Data Consuming System)

<table>
  <tr>
   <td><strong>Consent management use-cases</strong>
   </td>
   <td><strong>Link to the UCS</strong>
   </td>
  </tr>
  <tr>
   <td>AUDIT CONSENT - Query the Consents related to individuals or policies  (opt-in/opt-opt)
   </td>
   <td><a href="https://docs.google.com/document/d/1NyMTusB4V0TxJl7nWq7UsP92ZWiUVZivRaLU8CogKiw/edit?pli=1#bookmark=id.8o3vua71vfz2">UC-C-PIC-AT-001</a>
   </td>
  </tr>
  <tr>
   <td>MONITOR POLICY UPDATE- Tracking Data Policy changes and configuration conformance with it;
   </td>
   <td><a href="https://docs.google.com/document/d/1NyMTusB4V0TxJl7nWq7UsP92ZWiUVZivRaLU8CogKiw/edit?pli=1#bookmark=id.wzr0qjoqbl8c">UC-C-PIC-AT-002</a>
   </td>
  </tr>
  <tr>
   <td>READ CONSENT STATUS - Viewing (reading, exporting) the Consent Agreements and relevant reports in a verifiable form
   </td>
   <td><a href="https://docs.google.com/document/d/1NyMTusB4V0TxJl7nWq7UsP92ZWiUVZivRaLU8CogKiw/edit?pli=1#bookmark=id.zc71i2q4rzbf">UC-C-PIC-AT-003</a>
   </td>
  </tr>
  <tr>
   <td>VERIFY CONSENT INTEGRITY - Ability to check the integrity of the signed agreements
   </td>
   <td><a href="https://docs.google.com/document/d/1NyMTusB4V0TxJl7nWq7UsP92ZWiUVZivRaLU8CogKiw/edit?pli=1#bookmark=id.hcynqq227ezc">UC-C-PIC-AT-004</a>
   </td>
  </tr>
</table>

## 4.5	Scenarios: Consent and Data Access

As described above under [Universal Consenting Workflows](./9-workflows.md#44-universal-consent-workflows), there may be an unlimited number of business processes that require consent. The following scenarios are but a few examples illuminating how appropriate access to data can and should be handled when processing or consuming data with the support of Consent BB functionalities.

<table>
  <tr>
   <td><strong>Scenario</strong>
   </td>
   <td><strong>Source BB</strong>
   </td>
   <td><strong>Target BBs</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>1.1 Querying: Which Consent Agreement is needed for specified data processing/ consumption?
   </td>
   <td>Any
   </td>
   <td>Workflow BB
   </td>
   <td>Consent BB does have knowledge or state to resolve which Data Consumer or Data Producer requires consent. Everything regarding consent has a precondition that a decision is made and manifested in the Workflow BB or any other Data Consumer.
   </td>
  </tr>
  <tr>
   <td>1.2 Data processing/ consuming system stores/fetches data with consent + prompts the user if none exists
   </td>
   <td>Any
   </td>
   <td>Consent BB
   </td>
   <td>Given an Agreement ID and a User ID, the Consent BB can resolve if consent exists and possibly prompt the user. Workflow BB is especially inappropriate here because of UI integration and a blocking and sequential call stack.
   </td>
  </tr>
  <tr>
   <td>1.3 Data processing/ consuming system stores/ fetches data with consent, no halts operations without consent
   </td>
   <td>Any
   </td>
   <td>Workflow
   </td>
   <td>Given an Agreement ID and a User ID, the Workflow BB can complete an atomic action requiring consent. Operations shall not proceed if consent does not exist.
   </td>
  </tr>
  <tr>
   <td>1.4 Data processing/ consuming system stores/ fetches data with consent, consent is prompted asynchronously
   </td>
   <td>Any
   </td>
   <td>Workflow
   </td>
   <td>The Workflow BB may halt operations and asynchronously prompt the user for consent if none exists (or is invalid). After fetching consent, the Workflow BB should revert to the targeted data consuming/ processing operation.
   </td>
  </tr>
  <tr>
   <td>1.5 Appropriate access to data that does not require consent
   </td>
   <td>Any
   </td>
   <td>Workflow 
   </td>
   <td>Not necessarily related to Consent BB
   </td>
  </tr>
  <tr>
   <td>1.2-1.4 Side effects
   </td>
   <td>Workflow
   </td>
   <td>
   </td>
   <td>Any attempt to read consent and process/consume data is logged and auditable.
   </td>
  </tr>
  <tr>
   <td>2.1 Inappropriate access: Data processing/ consuming system inappropriately stores/ fetches data without consent
   </td>
   <td>Any
   </td>
   <td>n/a
   </td>
   <td>Any consent-requiring data access is assumed logged.
<p>
Auditing of inappropriate data access is only possible when a log trace exists.
   </td>
  </tr>
  <tr>
   <td>3.1
   </td>
   <td>Workflow
   </td>
   <td>Consent 
   </td>
   <td>Given an Individual, query if active Consent Records exist (for instance, to spot if other external data needs to be kept)
   </td>
  </tr>
  <tr>
   <td>4.1
   </td>
   <td>Any
   </td>
   <td>Consent
   </td>
   <td>Fundamental individual rights (GDPR / Data Protection Act etc): Right to be Forgotten
   </td>
  </tr>
  <tr>
   <td>4.x
   </td>
   <td>Any
   </td>
   <td>Consent
   </td>
   <td>Fundamental individual rights (GDPR / Data Protection Act etc): More TBD
   </td>
  </tr>
</table>