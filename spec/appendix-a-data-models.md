# 10 Appendix A: Data Models

API model schema can be found in the latest API definition in either of these resources:

* [https://docs.google.com/spreadsheets/d/1snIszqyTGYk1u25liwQ_1jONTsQeH7D8aqv1Td74xt4/edit#gid=1829058922](https://docs.google.com/spreadsheets/d/1snIszqyTGYk1u25liwQ_1jONTsQeH7D8aqv1Td74xt4/edit#gid=1829058922) _(**Note:** Please direct comments and suggestions to the working document)_
* [https://app.swaggerhub.com/apis/GovStack/consent-management-bb/](https://app.swaggerhub.com/apis/GovStack/consent-management-bb/) (interactive SwaggerHub OpenAPI rendition)
* [https://github.com/GovStackWorkingGroup/BuildingBlockAPI/pull/15](https://github.com/GovStackWorkingGroup/BuildingBlockAPI/pull/15) (source YAML files)

<table>
  <tr>
   <td>
<strong>Model</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Fields</strong>
   </td>
  </tr>
  <tr>
   <td>
    <code>Individual</code>
   </td>
   <td>Shallowly models an Individual which may reference some instance in an external system (registration system, functional ID, foundational ID etc). An Individual instance of this model is not to be mistaken with a unique natural individual. It is up to the system owner to decide if this record permits mapping to a natural individual and/or if a single Individual row can map to several consent agreements.
   </td>
   <td><code>id</code>, <code>functional_id</code>, <code>foundational_id</code>, <code>session_id</code>
   </td>
  </tr>
  <tr>
   <td><code>Agreement</code>
   </td>
   <td>An agreement contains the specification of a single purpose that can be consented to. An Agreement is universal and can be consented to by *many* individuals through a ConsentRecord
   </td>
   <td><code>id</code>, <code>version</code>, <code>controller</code>, <code>policy</code>, <code>purpose</code>, <code>lawful_basis</code>, <code>data_use</code>, <code>dpia</code>, <code>lifecycle</code>, <code>signature</code>, <code>active</code>, <code>forgettable</code>
   </td>
  </tr>
  <tr>
   <td><code>AgreementData</code>
   </td>
   <td>Agreement data contains specifications of exactly what is collected.
   </td>
   <td><code>id</code>, <code>agreement</code>, <code>name</code>, <code>sensitivity</code>, <code>category</code>, <code>hash</code>
   </td>
  </tr>
  <tr>
   <td><code>Policy</code>
   </td>
   <td>A policy governs data and Agreement in the realm of an organisation that is referred to as \"data controller\" (GDPR) and owner of referencing Agreements.
   </td>
   <td><code>id</code>, <code>name</code>, <code>version</code>, <code>url</code>, <code>jurisdiction</code>, <code>industry_sector</code>, <code>data_retention_period_days</code>, <code>geographic_restriction</code>, <code>storage_location</code>
   </td>
  </tr>
  <tr>
   <td><code>ConsentRecord</code>
   </td>
   <td>A Consent Record expresses consent (as defined in this building block's specification) to a single Agreement.
   </td>
   <td><code>id</code>, <code>agreement</code>, <code>agreement_revision</code>, <code>individual</code>, <code>opt_in</code>, <code>state</code>, <code>signature</code>
   </td>
  </tr>
  <tr>
   <td><code>Revision</code>
   </td>
   <td>A *generic* revision model captures the serialised contents of any schema's single row. This is then subject to 1) cryptographic signature and 2) auditing.
<p>
Aside from \"successor\" column, a revision should be considered locked.
   </td>
   <td><code>id</code>, <code>schema</code>, <code>object_id</code>, <code>serialized_snapshot</code>, <code>timestamp</code>, <code>authorized_by_individual</code>, <code>authorized_by_other</code>, <code>successor</code>, <code>predecessor_hash</code>, <code>predecessor_signature</code>
   </td>
  </tr>
  <tr>
   <td><code>AgreementFilter</code>
   </td>
   <td>Query filter for API endpoint listing Agreement objects
   </td>
   <td><code>id</code>, <code>name</code>
   </td>
  </tr>
  <tr>
   <td><code>ConsentRecordFilter</code>
   </td>
   <td>Query filter for API endpoint listing ConsentRecord objects
   </td>
   <td><code>id</code>, <code>opt_in</code>
   </td>
  </tr>
  <tr>
   <td><code>PolicyFilter</code>
   </td>
   <td>Query filter for API endpoint listing Policy objects
   </td>
   <td><code>id</code>, <code>name</code>, <code>revision</code>
   </td>
  </tr>
  <tr>
   <td><code>Controller</code>
   </td>
   <td>Details of a data controller.
   </td>
   <td><code>id</code>, <code>name</code>, <code>url</code>
   </td>
  </tr>
  <tr>
   <td><code>Signature</code>
   </td>
   <td>A generic signature contains a cryptographic hash of some value, together with a signature created by some private key in another system. Required signing methods: Revision object or another Signature object.
   </td>
   <td><code>id</code>, <code>verification_method</code>, <code>verification_hash</code>, <code>verification_signature</code>, <code>verification_artifact</code>, <code>jws_header</code>, <code>signed_by</code>, <code>timestamp</code>, <code>object_type</code>, <code>object_reference</code>
   </td>
  </tr>
  <tr>
   <td><code>AgreementPurpose</code>
   </td>
   <td>TBD: Models the purpose of an agreement
   </td>
   <td><code>id</code>, <code>name</code>, <code>description</code>
   </td>
  </tr>
  <tr>
   <td><code>AgreementLifecycle</code>
   </td>
   <td>TBD: Models the valid lifecycle states of an Agreement
   </td>
   <td><code>id</code>, <code>name</code>
   </td>
  </tr>
  <tr>
   <td><code>RegistryReference</code>
   </td>
   <td>TBD: When creating an Individual, we need some input that refers to a functional or foundational ID in an external system
   </td>
   <td><code>id</code>, <code>foundational_id</code>, <code>functional_id</code>
   </td>
  </tr>
  <tr>
   <td><code>AuditTracker</code>
   </td>
   <td>TBD: An external tracker receiving information from the system that can be subject to external auditing and verification of correct behaviour. This is one of several notification/monitor/subscription patterns that may be more suitable for an encrypted Pub/Sub service.
   </td>
   <td><code>id</code>, <code>name</code>, <code>public_key</code>, <code>callback_agreement</code>, <code>callback_consent_record</code>, <code>callback_policy</code>, <code>callback_revision_table_hash</code>, <code>callback_signature_table_hash</code>
   </td>
  </tr>
  <tr>
   <td><code>AuditEventType</code>
   </td>
   <td>TBD: Model for the possible events pertaining a change to an object subject to auditing. This model is not necessarily a database-backed model but part of application code.
   </td>
   <td><code>id</code>, <code>event_name</code>
   </td>
  </tr>
</table>

<!--
### TODO

All links above
-->