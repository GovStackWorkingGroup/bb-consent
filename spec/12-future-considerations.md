# 12 Our of Scope and Future Considerations

The following use cases are out of scope for this version 1.0 of Consent BB. These may be considered as potential future enhancements.

1. Non-reusable/single-action consent given in physical settings.

2. Consent to use data other than personal information on behalf of an organisation. For example, an organisation authorising an individual to consent to expose some organisation’s data is seen out of the scope of the consent building block.

3. Consent delegation: While being part of the Consent BB, this will be taken up in the future. For e.g. an individual is authorising another individual to consent on their behalf.

4. “Multi-Consent” is when consent **can** be given by more than one person or when consent is **required** to be given by more than one person. An example is given by the registration of a child whose consent is actually given by a parent or both in certain use cases. 

    In the current version of the specification, muti-consent can be implemented at the business process level, with multiple calls to the Consent BB. One call per consent transaction. In the future, it is planned to extend the functionalities of the BB to provide support for multi-consent.

5. Relationships between multiple Agreements will allow for a single transaction to capture an individual’s signature on multiple Agreements.

6. Consider individual rights (E.g. as per GDPR / Data Protection Act etc.), potentially amending Scenarios 4.x, API endpoints functionality and the capture of Consent Records.

   * The right to be informed
   * The right of access
   * The right to rectification
   * The right to erasure
   * The right to restrict processing
   * The right to data portability
   * The right to object
   * Rights about automated decision-making and profiling.

7. The elaborated lifecycle for Consent Agreement amendments: Data Policies and Consent Agreements may change over time. Such events are sensitive to existing Consent Records.

   * Notifications for any consent agreement changes; Individuals and Data Consuming and Data Providing Systems.
   * Notifications of Consent Record changes in bulk and separate: Data Consuming and Data Processing Systems.
   * All lifecycle events of Consent Agreements and Consent Records are mapped as Audit Event Types, and the external auditing system is notified.

8. Roles and scopes for IAM (Identity Management)  and RBAC to be used within consent BB

9.  We need to enable audit logging capabilities aligned with the overall GovStack goals. Issues to be addressed include audit log access control, the type of information captured in the audit log, and taking care of sensitive data or meaningful metadata.

10. Certain update use cases (e.g. modify consent agreement) might result in invalidating a previously acquired individual consent.  This will be investigated for future releases. 

11. Implicit or legitimate consent could be considered for future use cases and ultimately for the specification. There are scenarios where an implicit consent may require a verifiable transaction. There are also scenarios where tracking implicit consent in itself would constitute tracking, making this a complex field.
