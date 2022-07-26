# 7 Data Structures
<!--
{% hint style="info" %}

{% endhint %}
-->
## 7.1 Resource Model

The resource model shows the relationship between data objects that are used by this Building Block. Data objects are ultimately modelled as OpenAPI schemas, however as the relational model isn’t easy to understand from OpenAPI specification, we start by presenting two high-level Resource Models.
### 7.1.1 Simplified Resource Model

When an individual gives consent, it is implied that the Organisation from one side and the Individual from the other side digitally sign a Consent Agreement and a respective Consent Record is created. The alternative scenario may be that signing takes place offline on a paper, but in this case, for Consent BB to function properly, it is the responsibility of the Organisation to digitise (eg scan) the signed document and create digitally signed artefact to represent the Consent Record,

This Consent Record is a digital instance referencing the Agreement which is consented to or subsequently has consent withdrawn from. 

![alt_text](images/simple-resource-model.png "Simplified resource model")
[Diagram Source](https://github.com/GovStackWorkingGroup/BuildingBlockAPI/tree/main/consent-management)
### 7.1.2   Elaborated Resource Model

This model expands the relationships between resources.

Revisions are maintained for Consent Records + Agreements and Data Policies, together with cryptographic signatures. This means that all changes are captured for auditability.

For a configured Agreement, data elements requiring consent are individually specified as Agreement Data.. Agreement Data is not directly relatable to processes and internals of an external system: This architectural choice gives the consent model flexibility and greatly simplifies the architecture and consent lifecycle, but it does not contradict any additional features, allowing for relations to external systems.

![alt_text](images/elaborate-resource-model.png "Elaborated resource model")
[Diagram Source](https://github.com/GovStackWorkingGroup/BuildingBlockAPI/tree/main/consent-management)

## 7.2 Use cases informing events

Generic:
* Individual changes Consent Record
* Individual withdraws/revokes Consent Agreement
* Consent Record expires
* Consent Record expiry date changes
* Organisation replaces Consent Agreement
* Organisation replaces Data Policy

Specific Use Cases:
* Individual gives access to citizen data, using a third-party UI (Consumer’s UI). Example: COVID passports

## 7.3  Standards

The following standards are applicable to data structures in the registration building block:
* All dates should follow ISO 8601.
* RFC 7159 - The JavaScript Object Notation (JSON)
* OpenAPI Version 3.1.0
* RESTful APIs follow TM Forum Specification: “REST API Design Guidelines Part 1” (requirement derived from GovStack Architecture and Nonfunctional Requirements)

## 7.4 Data models

Data models are defined in [Appendix A: Data models](#heading=h.aq5kk1vg6pfe). This specification is seen as a minimum requirement, all further implementation may add more structure but should not compromise the minimal integrity laid out. All property types are generic, and a concrete implementation may add further specificity to these models.

The OpenAPI definition file is maintained in JSON format, and OpenAPI schemas may be interactively explored on Swagger Hub at [Consent BB](https://github.com/GovStackWorkingGroup/bb-consent)GitHub. 

<!--
### TODO

Fix Appendix A hyperlink

-->