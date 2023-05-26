{'openapi': '3.0.0', 'servers': [{'description': 'SwaggerHub API Auto Mocking', 'url': 'https://app.swaggerhub.com/apis/GovStack/consent-management-bb/'}], 'info': {'description': "This is a basic API for GovStack's Consent Building Block. It reflects the basic requirements of the Consent BB specification, which is versioned .", 'version': '1.1.0-rc1', 'title': 'Consent BB API', 'contact': {'email': 'balder@overtag.dk'}, 'license': {'name': 'Apache 2.0', 'url': 'http://www.apache.org/licenses/LICENSE-2.0.html'}}, 'tags': [{'name': 'org', 'description': 'Secured operations available to organization API integration'}, {'name': 'dataconsumer', 'description': 'Secured operations for data consumers and applications to verify consent'}, {'name': 'individual', 'description': 'Individual operations'}, {'name': 'auditor', 'description': 'Operations for external auditing systems to query detailed data from the system and subscribe to notifications.'}, {'name': 'notification', 'description': 'Subscribe/unsubscribe notifications for data processors, consumers and frontend systems for individuals.'}, {'name': 'callback', 'description': 'Callback API for other Building Blocks, especially relevant for asynchronous processes.'}], 'paths': {'/config/policy/': {'post': {'tags': ['config'], 'summary': 'CREATE - Creates a new Policy object and returns the new object and a PolicyRevision', 'operationId': 'configPolicyCreate', 'description': 'CREATE - Creates a new Policy object and returns the new object and a PolicyRevision', 'parameters': [{'in': 'query', 'name': 'Policy', 'description': 'An object of type Policy', 'required': True, 'schema': {'$ref': '#/components/schemas/Policy'}}], 'x-specification-usecase': 'UC-C-PIC-A-001', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': 'A set consisting of the new Policy object created, together with the initial Revision object.', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Policy'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/config/policy/{policyId}/': {'get': {'tags': ['config'], 'summary': 'READ - get a Policy object + latest Revision. If a PolicyFilter is supplied and contains a revision_id, then this specific revision is returned.', 'operationId': 'orgReadPolicy', 'description': 'READ - get a Policy object + latest Revision. If a PolicyFilter is supplied and contains a revision_id, then this specific revision is returned.', 'parameters': [{'in': 'path', 'name': 'policyId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'PolicyFilter', 'description': 'An object of type PolicyFilter', 'required': True, 'schema': {'$ref': '#/components/schemas/PolicyFilter'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Policy'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/config/policy/{policyId}/revisions/': {'get': {'tags': ['config'], 'summary': 'LIST - returns the current Policy', 'operationId': 'orgListPolicyRevisions', 'description': 'LIST - returns the current Policy', 'parameters': [{'in': 'path', 'name': 'policyId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Policy'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/config/policy/{id}/': {'put': {'tags': ['config'], 'summary': 'UPDATE - Updates an existing Policy object, returning the updated version and a new revision. Updating a Policy does not affect existing references in Agreement, the new revision should be specified for Agreement.', 'operationId': 'orgUpdatePolicy', 'description': 'UPDATE - Updates an existing Policy object, returning the updated version and a new revision. Updating a Policy does not affect existing references in Agreement, the new revision should be specified for Agreement.', 'parameters': [{'in': 'path', 'name': 'id', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'Policy', 'description': 'An object of type Policy', 'required': True, 'schema': {'$ref': '#/components/schemas/Policy'}}], 'x-specification-usecase': 'UC-C-PIC-A-002', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Policy'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}, 'delete': {'tags': ['config'], 'summary': "DELETE - Deletes an existing Policy object, returning the updated version and a new revision. Deleting a Policy is not possible if it's associated with active Agreement.", 'operationId': 'orgDeletePolicy', 'description': "DELETE - Deletes an existing Policy object, returning the updated version and a new revision. Deleting a Policy is not possible if it's associated with active Agreement.", 'parameters': [{'in': 'path', 'name': 'id', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-A-004', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Revision'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/config/policies/': {'get': {'tags': ['config'], 'summary': 'Returns a list of readable Policy objects', 'operationId': 'orgListPolicy', 'description': 'LIST - Fetches list of readable Policy objects', 'parameters': [{'in': 'query', 'name': 'PolicyFilter', 'description': 'An object of type PolicyFilter', 'required': True, 'schema': {'$ref': '#/components/schemas/PolicyFilter'}}, {'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': 'UC-C-PIC-A-001, UC-C-PIC-A-002', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': "A list of Policy objects readable for the current session's credentials.", 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Policy'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['admin']}]}}, '/config/agreement/{agreementId}/': {'get': {'tags': ['config'], 'summary': 'READ - fetches the latest version of an Agreement', 'operationId': 'configAgreementRead', 'description': 'READ - fetches the latest version of an Agreement', 'parameters': [{'in': 'path', 'name': 'agreementId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Agreement'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}, 'put': {'tags': ['config'], 'summary': 'UPDATE - An existing Agreement object is created and returned together with AgreementRevision', 'operationId': 'orgUpdateAgreement', 'description': 'UPDATE - An existing Agreement object is created and returned together with AgreementRevision', 'parameters': [{'in': 'path', 'name': 'agreementId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'Agreement', 'description': 'An object of type Agreement', 'required': True, 'schema': {'$ref': '#/components/schemas/Agreement'}}], 'x-specification-usecase': 'UC-C-PIC-A-002', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Agreement'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}, 'delete': {'tags': ['config'], 'summary': '', 'operationId': 'orgDeleteAgreement', 'description': '', 'parameters': [{'in': 'path', 'name': 'agreementId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-A-004', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Revision'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/config/agreement/': {'post': {'tags': ['config'], 'summary': 'CREATE - A new Agreement object is created and returned together with AgreementRevision', 'operationId': 'orgCreateAgreement', 'description': 'CREATE - A new Agreement object is created and returned together with AgreementRevision', 'parameters': [{'in': 'query', 'name': 'Agreement', 'description': 'An object of type Agreement', 'required': True, 'schema': {'$ref': '#/components/schemas/Agreement'}}], 'x-specification-usecase': 'UC-C-PIC-A-001', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Agreement'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/config/agreements/': {'get': {'tags': ['config'], 'summary': '', 'operationId': 'orgListAgreement', 'description': '', 'parameters': [{'in': 'query', 'name': 'AgreementFilter', 'description': 'An object of type AgreementFilter', 'required': True, 'schema': {'$ref': '#/components/schemas/AgreementFilter'}}, {'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Agreement'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/service/individual/': {'post': {'tags': ['service'], 'summary': 'CREATE - Creates an Individual in the Consent system', 'operationId': 'orgIndividualCreate', 'description': 'CREATE - Creates an Individual in the Consent system', 'parameters': [{'in': 'query', 'name': 'RegistryReference', 'description': 'An object of type RegistryReference', 'required': True, 'schema': {'$ref': '#/components/schemas/RegistryReference'}}], 'x-specification-usecase': '', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Individual'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/service/individual/{individualId}/': {'get': {'tags': ['service'], 'summary': 'READ - Fetch an Individual in the Consent system', 'operationId': 'orgIndividualRead', 'description': 'READ - Fetch an Individual in the Consent system', 'parameters': [{'in': 'path', 'name': 'individualId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': '', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Individual'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}, 'put': {'tags': ['service'], 'summary': 'UPDATE - Updates an Individual in the Consent system', 'operationId': 'orgIndividualUpdate', 'description': 'UPDATE - Updates an Individual in the Consent system', 'parameters': [{'in': 'path', 'name': 'individualId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': '', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Individual'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}, 'delete': {'tags': ['service'], 'summary': 'DELETE - entirely removes an individual from the system and cascades necessary actions to related ConsentRecord objects', 'operationId': 'orgIndividualDelete', 'description': 'DELETE - entirely removes an individual from the system and cascades necessary actions to related ConsentRecord objects', 'parameters': [{'in': 'path', 'name': 'individualId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': '', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Individual'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/service/individuals/': {'get': {'tags': ['service'], 'summary': 'LIST - lists individuals in the system', 'operationId': 'orgIndividualList', 'description': 'LIST - lists individuals in the system', 'parameters': [{'in': 'query', 'name': 'RegistryReference', 'description': 'An object of type RegistryReference', 'required': True, 'schema': {'$ref': '#/components/schemas/RegistryReference'}}, {'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': '', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Individual'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/service/agreement/{agreementId}/': {'get': {'tags': ['service'], 'summary': 'READ - fetches the latest version of an Agreement', 'operationId': 'serviceAgreementRead', 'description': 'READ - fetches the latest version of an Agreement', 'parameters': [{'in': 'path', 'name': 'agreementId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Agreement'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/service/policy/{policyId}/': {'get': {'tags': ['service'], 'summary': 'READ - fetches the latest version of a Policy', 'operationId': 'servicePolicyRead', 'description': 'READ - fetches the latest version of a Policy', 'parameters': [{'in': 'path', 'name': 'policyId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Policy'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/service/purpose/{purposeId}/': {'get': {'tags': ['service'], 'summary': 'READ - fetches the latest version of an AgreementPurpose', 'operationId': 'serviceAgreementPurposeRead', 'description': 'READ - fetches the latest version of an AgreementPurpose', 'parameters': [{'in': 'path', 'name': 'purposeId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/AgreementPurpose'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/service/agreement/{agreementId}/agreementdata/': {'get': {'tags': ['service'], 'summary': 'READ - fetches a list of latest versions of AgreementData associated with an Agreement', 'operationId': 'serviceAgreementDataRead', 'description': 'READ - fetches a list of latest versions of AgreementData associated with an Agreement', 'parameters': [{'in': 'path', 'name': 'agreementId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/AgreementData'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['org']}]}}, '/service/verification/agreements/': {'get': {'tags': ['service'], 'summary': 'LIST - Fetch consent records for suplied AgreementFilter', 'operationId': 'serviceVerificationAgreementList', 'description': 'LIST - Fetch consent records for suplied AgreementFilter', 'parameters': [{'in': 'query', 'name': 'AgreementFilter', 'description': 'An object of type AgreementFilter', 'required': True, 'schema': {'$ref': '#/components/schemas/AgreementFilter'}}, {'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '1.1', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/ConsentRecord'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['consumer']}]}}, '/service/verification/agreement/{agreementId}/': {'get': {'tags': ['service'], 'summary': 'READ - Fetch a specific Consent Record (latest revision). Individual ID supplied as HTTP header.', 'operationId': 'serviceVerificationAgreementConsentRecordRead', 'description': 'READ - Fetch a specific Consent Record (latest revision). Individual ID supplied as HTTP header.', 'parameters': [{'in': 'path', 'name': 'agreementId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '1.2', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/ConsentRecord'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['consumer']}]}}, '/service/verification/consentrecords/': {'get': {'tags': ['service'], 'summary': 'LIST - Fetch consent records (latest revision). For a given Agreement and Individual, query if consent exists', 'operationId': 'serviceVerificationConsentRecordList', 'description': 'LIST - Fetch consent records (latest revision). For a given Agreement and Individual, query if consent exists', 'parameters': [{'in': 'query', 'name': 'ConsentRecordFilter', 'description': 'An object of type ConsentRecordFilter', 'required': True, 'schema': {'$ref': '#/components/schemas/ConsentRecordFilter'}}, {'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': 'UC-C-PIC-A-003', 'x-specification-scenario': '3.1, 1.2', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/ConsentRecord'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['consumer']}]}}, '/service/individual/record/agreement/{agreementId}/': {'post': {'tags': ['service'], 'summary': 'CREATE - For a particular Individual and a particular Agreement, create a new Consent Record pointing to the current Revision of a given Agreement. Individual ID supplied as HTTP header.', 'operationId': 'serviceCreateIndividualConsentRecord', 'description': 'CREATE - For a particular Individual and a particular Agreement, create a new Consent Record pointing to the current Revision of a given Agreement. Individual ID supplied as HTTP header.', 'parameters': [{'in': 'path', 'name': 'agreementId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'individualId', 'description': 'An object with id individualId', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'agreementId', 'description': 'An object with id agreementId', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'revisionId', 'description': 'An object with id revisionId', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-I-002', 'x-specification-scenario': '1.2', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/ConsentRecord'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['individual']}]}, 'get': {'tags': ['service'], 'summary': 'READ - Individual ID supplied as HTTP header. Fetches the current ConsentRecord for an Agreement. There should be one unambiguous ConsentRecord for an Individual and an Agreement.', 'operationId': 'serviceReadIndividualRecordRead', 'description': 'READ - Individual ID supplied as HTTP header. Fetches the current ConsentRecord for an Agreement. There should be one unambiguous ConsentRecord for an Individual and an Agreement.', 'parameters': [{'in': 'path', 'name': 'agreementId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-I-001', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ConsentRecord'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['individual']}]}}, '/service/individual/record/consentrecord/draft/': {'post': {'tags': ['service'], 'summary': 'CREATE - Gets a DRAFT (unsaved) ConsentRecord and Signature objects (without a PK) for a given agreementId.', 'operationId': 'serviceCreateIndividualConsentRecordDraft', 'description': 'CREATE - Gets a DRAFT (unsaved) ConsentRecord and Signature objects (without a PK) for a given agreementId.', 'parameters': [{'in': 'query', 'name': 'individualId', 'description': 'An object with id individualId', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'agreementId', 'description': 'An object with id agreementId', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'revisionId', 'description': 'An object with id revisionId', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-I-002', 'x-specification-scenario': '1.2', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/ConsentRecord'}, {'$ref': '#/components/schemas/Signature'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['individual']}]}}, '/service/individual/record/consentrecord/': {'post': {'tags': ['service'], 'summary': 'CREATE - Creates a paired ConsentRecord and Signature object. Returns the same objects with the PK defined.', 'operationId': 'serviceCreateIndividualConsentRecordAndSignature', 'description': 'CREATE - Creates a paired ConsentRecord and Signature object. Returns the same objects with the PK defined.', 'parameters': [{'in': 'query', 'name': 'ConsentRecord', 'description': 'An object of type ConsentRecord', 'required': True, 'schema': {'$ref': '#/components/schemas/ConsentRecord'}}, {'in': 'query', 'name': 'Signature', 'description': 'An object of type Signature', 'required': True, 'schema': {'$ref': '#/components/schemas/Signature'}}], 'x-specification-usecase': 'UC-C-PIC-I-002', 'x-specification-scenario': '1.2', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/ConsentRecord'}, {'$ref': '#/components/schemas/Signature'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['individual']}]}}, '/service/individual/record/consentrecord/{consentRecordId}/': {'put': {'tags': ['service'], 'summary': 'UPDATE* - Update a particular Consent Record. Individual ID supplied as HTTP header. Note that updating a signed Consent Record invalidates its signature.', 'operationId': 'serviceUpdateIndividualConsentRecord', 'description': 'UPDATE* - Update a particular Consent Record. Individual ID supplied as HTTP header. Note that updating a signed Consent Record invalidates its signature.', 'parameters': [{'in': 'path', 'name': 'consentRecordId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'Individual', 'description': 'An object of type Individual', 'required': True, 'schema': {'$ref': '#/components/schemas/Individual'}}, {'in': 'query', 'name': 'Agreement', 'description': 'An object of type Agreement', 'required': True, 'schema': {'$ref': '#/components/schemas/Agreement'}}, {'in': 'query', 'name': 'Revision', 'description': 'An object of type Revision', 'required': True, 'schema': {'$ref': '#/components/schemas/Revision'}}], 'x-specification-usecase': 'UC-C-PIC-I-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/ConsentRecord'}, {'$ref': '#/components/schemas/Revision'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['individual']}]}}, '/service/individual/record/consentrecord/{consentRecordId}/signature/': {'post': {'tags': ['service'], 'summary': 'CREATE - Creates and returns a blank Signature object for the Consent Record.', 'operationId': 'serviceCreateIndividualConsentRecordSignature', 'description': 'CREATE - Creates and returns a blank Signature object for the Consent Record.', 'parameters': [{'in': 'path', 'name': 'consentRecordId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-Post-Partum-001-Registration_PostPartum_and_InfantCare', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Signature'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['individual']}]}, 'put': {'tags': ['service'], 'summary': 'UPDATE - Updates a Signature object for a Consent Record. This is used to add a signature to an existing unsigned Signature object. Consent BB is responsible for updating the Consent Record state.', 'operationId': 'serviceUpdateIndividualConsentRecordSignature', 'description': 'UPDATE - Updates a Signature object for a Consent Record. This is used to add a signature to an existing unsigned Signature object. Consent BB is responsible for updating the Consent Record state.', 'parameters': [{'in': 'path', 'name': 'consentRecordId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'Signature', 'description': 'An object of type Signature', 'required': True, 'schema': {'$ref': '#/components/schemas/Signature'}}], 'x-specification-usecase': 'UC-Post-Partum-001-Registration_PostPartum_and_InfantCare', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Signature'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['individual']}]}}, '/service/individual/record/agreement/': {'get': {'tags': ['service'], 'summary': 'LIST - Individual ID supplied as HTTP header.', 'operationId': 'serviceListIndividualRecordList', 'description': 'LIST - Individual ID supplied as HTTP header.', 'parameters': [{'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': 'UC-C-PIC-I-001', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/ConsentRecord'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['individual']}]}}, '/service/individual/record/': {'delete': {'tags': ['service'], 'summary': 'DELETE - Cascading delete operation for Right To Be Forgotten, deletes all Consent Records that shall not be retained and have a "forgettable" Agreement. May also delete an unsigned Consent Record, for instance in cases where the user exits the signing process. Individual ID supplied as HTTP header.', 'operationId': 'serviceDeleteAllRecords', 'description': 'DELETE - Cascading delete operation for Right To Be Forgotten, deletes all Consent Records that shall not be retained and have a "forgettable" Agreement. May also delete an unsigned Consent Record, for instance in cases where the user exits the signing process. Individual ID supplied as HTTP header.', 'parameters': [], 'x-specification-usecase': 'UC-C-PIC-I-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'True', 'responses': {'200': {'description': ''}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': ['individual']}]}}, '/audit/trackers/': {'get': {'tags': ['auditor'], 'summary': 'LIST - show available AuditTracker objects', 'operationId': 'auditListTrackers', 'description': 'LIST - show available AuditTracker objects', 'parameters': [{'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': 'UC-C-PIC-AT-001, UC-C-PIC-AT-002', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/AuditTracker'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}}, '/audit/tracker/': {'post': {'tags': ['auditor'], 'summary': 'CREATE - A new AuditTracker is set up', 'operationId': 'auditCreateTracker', 'description': 'CREATE - A new AuditTracker is set up', 'parameters': [{'in': 'query', 'name': 'AuditTracker', 'description': 'An object of type AuditTracker', 'required': True, 'schema': {'$ref': '#/components/schemas/AuditTracker'}}], 'x-specification-usecase': 'UC-C-PIC-AT-001, UC-C-PIC-AT-002', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/AuditTracker'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}}, '/audit/tracker/{trackerId}/': {'get': {'tags': ['auditor'], 'summary': 'READ - get the details of an AuditTracker', 'operationId': 'auditReadTracker', 'description': 'READ - get the details of an AuditTracker', 'parameters': [{'in': 'path', 'name': 'trackerId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-AT-001, UC-C-PIC-AT-002', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/AuditTracker'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}, 'put': {'tags': ['auditor'], 'summary': 'UPDATE - get the details of an AuditTracker', 'operationId': 'auditUpdateTracker', 'description': 'UPDATE - get the details of an AuditTracker', 'parameters': [{'in': 'path', 'name': 'trackerId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'AuditTracker', 'description': 'An object of type AuditTracker', 'required': True, 'schema': {'$ref': '#/components/schemas/AuditTracker'}}], 'x-specification-usecase': 'UC-C-PIC-AT-001, UC-C-PIC-AT-002', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/AuditTracker'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}, 'delete': {'tags': ['auditor'], 'summary': 'DELETE - removes an AuditTracker', 'operationId': 'auditDeleteTracker', 'description': 'DELETE - removes an AuditTracker', 'parameters': [{'in': 'path', 'name': 'trackerId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}], 'x-specification-usecase': 'UC-C-PIC-AT-001, UC-C-PIC-AT-002', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/AuditTracker'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}}, '/audit/consentrecords/': {'get': {'tags': ['auditor'], 'summary': 'LIST - fetch ConsentRecord objects', 'operationId': 'auditConsentRecordList', 'description': 'LIST - fetch ConsentRecord objects', 'parameters': [{'in': 'query', 'name': 'ConsentRecordFilter', 'description': 'An object of type ConsentRecordFilter', 'required': True, 'schema': {'$ref': '#/components/schemas/ConsentRecordFilter'}}, {'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': 'UC-C-PIC-AT-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/ConsentRecord'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}}, '/audit/consentrecord/{consentRecordId}/': {'get': {'tags': ['auditor'], 'summary': 'READ', 'operationId': 'auditConsentRecordRead', 'description': 'READ', 'parameters': [{'in': 'path', 'name': 'consentRecordId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'ConsentRecord', 'description': 'An object of type ConsentRecord', 'required': True, 'schema': {'$ref': '#/components/schemas/ConsentRecord'}}], 'x-specification-usecase': '', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/ConsentRecord'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}}, '/audit/agreements/': {'get': {'tags': ['auditor'], 'summary': '', 'operationId': 'auditAgreementList', 'description': '', 'parameters': [{'in': 'query', 'name': 'AgreementFilter', 'description': 'An object of type AgreementFilter', 'required': True, 'schema': {'$ref': '#/components/schemas/AgreementFilter'}}, {'in': 'query', 'name': 'offset', 'description': 'Requested index for start of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}, {'in': 'query', 'name': 'limit', 'description': 'Requested number of resources to be provided in response requested by client', 'required': False, 'schema': {'type': 'integer'}}], 'x-specification-usecase': 'UC-C-PIC-AT-001, UC-C-PIC-AT-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'type': 'array', 'items': {'oneOf': [{'$ref': '#/components/schemas/Agreement'}]}}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}}, '/audit/agreement/{agreementId}/': {'get': {'tags': ['auditor'], 'summary': 'READ', 'operationId': 'auditReadRecord', 'description': 'READ', 'parameters': [{'in': 'path', 'name': 'agreementId', 'description': 'Unique ID of an object', 'required': True, 'schema': {'type': 'string'}}, {'in': 'query', 'name': 'AgreementFilter', 'description': 'An object of type AgreementFilter', 'required': True, 'schema': {'$ref': '#/components/schemas/AgreementFilter'}}], 'x-specification-usecase': 'UC-C-PIC-AT-001, UC-C-PIC-AT-003', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/Agreement'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}}, '/status/startup/': {'get': {'tags': ['status'], 'summary': 'READ', 'operationId': 'statusStartup', 'description': 'READ', 'parameters': [], 'x-specification-usecase': '', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/StatusStartup'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}}, '/status/readiness/': {'get': {'tags': ['status'], 'summary': 'READ', 'operationId': 'StatusReadiness', 'description': 'READ', 'parameters': [], 'x-specification-usecase': '', 'x-specification-scenario': '', 'x-specification-pii-or-sensitive': 'False', 'responses': {'200': {'description': '', 'content': {'application/json': {'schema': {'$ref': '#/components/schemas/StatusRediness'}}}}, '400': {'description': 'bad input parameter'}}, 'security': [{'OAuth2': []}]}}}, 'components': {'schemas': {'Individual': {'type': 'object', 'description': 'Shallowly models an Individual which may reference some instance in an external system (registration system, functional ID, foundational ID etc). An Individual instance of this model is not to be mistaken with a unique natural individual. It is up to the system owner to decide if this record permits mapping to a natural individual and/or if a single Individual row can map to several consent agreements.', 'required': ['id', 'external_id', 'external_id_type', 'identity_provider_id'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': 'The unique ID of an Individual row.'}, 'external_id': {'type': 'string', 'format': '', 'example': '', 'description': 'Reference to another foundational/functional ID, which is likely PII'}, 'external_id_type': {'type': 'string', 'format': '', 'example': '', 'description': 'External id type specifier. A string. For instance "email" or "foundational id". Can be used in later queries.'}, 'identity_provider_id': {'type': 'string', 'format': '', 'example': '', 'description': 'This could be an FK, but for now we do not have a mapping of identity providers. IDBB may have more requirements.'}}}, 'Agreement': {'type': 'object', 'description': 'An agreement contains the specification of a single purpose that can be consented to. An Agreement is universal and can be consented to by *many* individuals through a ConsentRecord', 'required': ['id', 'version', 'controller', 'policy', 'purpose', 'lawful_basis', 'data_use', 'dpia', 'lifecycle', 'signature', 'active', 'forgettable'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'version': {'type': 'string', 'format': '', 'example': '', 'description': 'The version of this specification to which a receipt conforms'}, 'controller': {'$ref': '#/components/schemas/Controller'}, 'policy': {'$ref': '#/components/schemas/Policy'}, 'purpose': {'$ref': '#/components/schemas/AgreementPurpose'}, 'lawful_basis': {'type': 'string', 'format': '', 'example': '', 'description': 'Lawful basis of the agreement - consent / legal_obligation / contract / vital_interest / public_task / legitimate_interest'}, 'data_use': {'type': 'string', 'format': '', 'example': '', 'description': 'null/data-source/data-using-service'}, 'dpia': {'type': 'string', 'format': '', 'example': '', 'description': 'Data Protection Impact Assessment'}, 'lifecycle': {'$ref': '#/components/schemas/AgreementLifecycle'}, 'signature': {'$ref': '#/components/schemas/Signature'}, 'active': {'type': 'boolean', 'format': '', 'example': '', 'description': 'Agreement is active and new ConsentRecords can be created.'}, 'forgettable': {'type': 'boolean', 'format': '', 'example': '', 'description': 'Consent Record may be deleted when consent is withdrawn, as its existence is not necessary for auditability.'}}}, 'AgreementData': {'type': 'object', 'description': 'Agreement data contains specifications of exactly what is collected.', 'required': ['id', 'agreement', 'name', 'sensitivity', 'category', 'hash'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'agreement': {'$ref': '#/components/schemas/Agreement'}, 'name': {'type': 'string', 'format': '', 'example': '', 'description': 'Name of the attribute, for instance "name" or "age"'}, 'sensitivity': {'type': 'string', 'format': '', 'example': '', 'description': 'categories of sensitivity'}, 'category': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'hash': {'type': 'string', 'format': '', 'example': '', 'description': 'In order to sign an Agreement, this relation needs to have a cryptopgraphic hash to be included in the Signature of the Agreement.'}}}, 'Policy': {'type': 'object', 'description': 'A policy governs data and Agreement in the realm of an organisation that is refered to as "data controller" (GDPR) and owner of referencing Agreements.', 'required': ['id', 'name', 'version', 'url', 'jurisdiction', 'industry_sector', 'data_retention_period_days', 'geographic_restriction', 'storage_location'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'name': {'type': 'string', 'format': '', 'example': '', 'description': 'Name of the policy'}, 'version': {'type': 'string', 'format': '', 'example': '', 'description': 'Version of the policy'}, 'url': {'type': 'string', 'format': '', 'example': '', 'description': 'Permanent URL at which this very version of the Policy can be read, should not be allowed to change over time.'}, 'jurisdiction': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'industry_sector': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'data_retention_period_days': {'type': 'integer', 'format': '', 'example': '', 'description': ''}, 'geographic_restriction': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'storage_location': {'type': 'string', 'format': '', 'example': '', 'description': ''}}}, 'ConsentRecord': {'type': 'object', 'description': "A Consent Record expresses consent (as defined in this building block's specification) to a single Agreement. There must be a UNIQUE constraint on (agreement_revision, individual)", 'required': ['id', 'agreement', 'agreement_revision', 'individual', 'opt_in', 'state', 'signature'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': 'Objects may be passed back by some API endpoints without an id (PK), denoting that they are a "draft", i.e. a ConsentRecord that is not yet stored in the database and only exist in transit. Draft ConsentRecords do not have a Revision, but if paired up with a Signature, a valid Revision should be generated.'}, 'agreement': {'$ref': '#/components/schemas/Agreement'}, 'agreement_revision': {'$ref': '#/components/schemas/Revision'}, 'individual': {'$ref': '#/components/schemas/Individual'}, 'opt_in': {'type': 'boolean', 'format': '', 'example': '', 'description': 'True: The individual has positively opted in. False: The individual has explicitly said no (or withdrawn a previous consent).'}, 'state': {'type': 'string', 'format': '', 'example': '', 'description': 'The state field is used to record state changes after-the-fact. It is maintained by the Consent BB itself. Valid states: unsigned/pending more signatures/signed'}, 'signature': {'$ref': '#/components/schemas/Signature'}}}, 'Revision': {'type': 'object', 'description': 'A *generic* revision model captures the serialized contents of any shema\'s single row. This is then subject to 1) cryptographic signature and 2) auditing.\n\nAside from "successor" column, a revision should be considered locked.', 'required': ['id', 'schema', 'object_id', 'serialized_snapshot', 'timestamp', 'authorized_by_individual', 'authorized_by_other', 'successor', 'predecessor_hash', 'predecessor_signature'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'schema': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'object_id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'serialized_snapshot': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'timestamp': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'authorized_by_individual': {'$ref': '#/components/schemas/Individual'}, 'authorized_by_other': {'type': 'string', 'format': '', 'example': '', 'description': 'Reference to an admin user that has created this revision'}, 'successor': {'$ref': '#/components/schemas/Revision'}, 'predecessor_hash': {'type': 'string', 'format': '', 'example': '', 'description': 'Tamper-resistent artifact from previous record'}, 'predecessor_signature': {'type': 'string', 'format': '', 'example': '', 'description': "Tamper-resistent artifact from previous record (we don't know if the previous record was signed or not)"}}}, 'AgreementFilter': {'type': 'object', 'description': 'Query filter for API endpoint listing Agreement objects', 'required': ['id', 'name'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'name': {'type': 'string', 'format': '', 'example': '', 'description': ''}}}, 'ConsentRecordFilter': {'type': 'object', 'description': 'Query filter for API endpoint listing ConsentRecord objects', 'required': ['id', 'opt_in', 'agreement', 'agreement_revision', 'individual', 'functional_id', 'foundational_id'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'opt_in': {'type': 'boolean', 'format': '', 'example': '', 'description': ''}, 'agreement': {'$ref': '#/components/schemas/Agreement'}, 'agreement_revision': {'$ref': '#/components/schemas/Revision'}, 'individual': {'$ref': '#/components/schemas/Individual'}, 'functional_id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'foundational_id': {'type': 'string', 'format': '', 'example': '', 'description': ''}}}, 'PolicyFilter': {'type': 'object', 'description': 'Query filter for API endpoint listing Policy objects', 'required': ['id', 'name', 'revision'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'name': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'revision': {'$ref': '#/components/schemas/Revision'}}}, 'Controller': {'type': 'object', 'description': 'Details of a data controller.', 'required': ['id', 'name', 'url'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'name': {'type': 'string', 'format': '', 'example': '', 'description': 'Name of data controller (may be omitted if no data involved)'}, 'url': {'type': 'string', 'format': '', 'example': '', 'description': 'URL of data controller (may be omitted if no data involved)'}}}, 'Signature': {'type': 'object', 'description': 'A generic signature contains a cryptographic hash of some value, together with a signature created by some private key in another system. Required signing methods: Revision object or another Signature object.', 'required': ['id', 'payload', 'signature', 'verification_method', 'verification_hash', 'verification_artifact', 'verification_signed_by', 'verification_jws_header', 'timestamp', 'object_type', 'object_reference'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': 'Objects may be passed back by some API endpoints without an id (PK), denoting that they are a "draft", i.e. a Signature that is not yet stored in the database and only exist in transit.'}, 'payload': {'type': 'string', 'format': '', 'example': '', 'description': 'The payload that is signed, constructed as a serialization of fields verification_method + verification_hash + verification_artifact + verification_signed_by + verification_jws_header. Serialized as a JSON dict.'}, 'signature': {'type': 'string', 'format': '', 'example': '', 'description': 'Signature (of payload), the format of the signature should be specified by either verification_method or verification_jws_header'}, 'verification_method': {'type': 'string', 'format': '', 'example': '', 'description': 'A well-known string denoting which method is used. Valid values: <TBD>. We might expand this with a relation to which verification methods that are supported. There may be a minimal set of supported methods necessary.'}, 'verification_hash': {'type': 'string', 'format': '', 'example': '', 'description': 'Internally generated cryptographic hash of the value to be signed. The hash is (re)produced from the object_type and object_reference - but from the serialized data of those.'}, 'verification_artifact': {'type': 'string', 'format': '', 'example': '', 'description': 'A verification artifact in the form of a scanned object, image, signature etc.'}, 'verification_signed_by': {'type': 'string', 'format': '', 'example': '', 'description': "Because an identifier's information may change over time, there is a need to store that information at the time of signing. In case of a cryptographic signature, this field should contain some identifier for looking up or verifying the public key of the signing party. In case of a non-cryptographic signature, this field could contain a natural individual's names, personal number, email addresses - store a snapshot that binds to the signature at the time of signing. In case of a cryptographic signature, this may be the fingerprint of the individual's public key or in some cases, a token from the user's ID session."}, 'verification_jws_header': {'type': 'string', 'format': '', 'example': '', 'description': 'Alternative to the verification_method, verification_hash and verification_signature, give a JWS serialized object (RFC7515)'}, 'timestamp': {'type': 'string', 'format': '', 'example': '', 'description': "Timestamp of signature, currently this field isn't part of the payload so it's not tamper-proof."}, 'object_type': {'type': 'string', 'format': '', 'example': '', 'description': 'Name of the schema model that object_reference points to. Values: "signature" or "revision"'}, 'object_reference': {'type': 'string', 'format': '', 'example': '', 'description': 'A symmetric relation / back reference to the object_type that was signed. We are currently just modelling signing another signature (a chain) or signing a Revision (which can be a revision of a consent record, an agreement, policy etc)'}}}, 'AgreementPurpose': {'type': 'object', 'description': 'TBD: Models the purpose of an agreement', 'required': ['id', 'name', 'description', 'hash'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'name': {'type': 'string', 'format': '', 'example': '', 'description': 'Name of purpose'}, 'description': {'type': 'string', 'format': '', 'example': '', 'description': 'Description of purpose'}, 'hash': {'type': 'string', 'format': '', 'example': '', 'description': 'In order to sign an Agreement, this relation needs to have a cryptopgraphic hash to be included in the Signature of the Agreement.'}}}, 'AgreementLifecycle': {'type': 'object', 'description': 'TBD: Models the valid lifecycle states of an Agreement', 'required': ['id', 'name'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'name': {'type': 'string', 'format': '', 'example': '', 'description': 'Definition / Preparation / Capture / Use / Proof'}}}, 'RegistryReference': {'type': 'object', 'description': 'TBD: When creating an Invidiual, we need some input that refers to a functional or foundational ID in an external system', 'required': ['id', 'foundational_id', 'functional_id'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'foundational_id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'functional_id': {'type': 'string', 'format': '', 'example': '', 'description': ''}}}, 'AuditTracker': {'type': 'object', 'description': 'TBD: An external tracker receiving information from the system that can be subject to external auditing and verification of correct behavior. This is one of several notification/monitor/subscription patterns that may be more suitable for an encrypted Pub/Sub service.', 'required': ['id', 'name', 'public_key', 'callback_agreement', 'callback_consent_record', 'callback_policy', 'callback_revision_table_hash', 'callback_signature_table_hash'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'name': {'type': 'string', 'format': '', 'example': '', 'description': 'Name of the auditing system'}, 'public_key': {'type': 'string', 'format': '', 'example': '', 'description': "The auditing system's public key for encrypting data sent to callback functions"}, 'callback_agreement': {'type': 'string', 'format': '', 'example': '', 'description': 'A URL receiving a callback with the Agreement object + Revision + AuditEventType'}, 'callback_consent_record': {'type': 'string', 'format': '', 'example': '', 'description': 'A URL receiving a callback with the ConsentRecord object + Revision + AuditEventType'}, 'callback_policy': {'type': 'string', 'format': '', 'example': '', 'description': 'A URL receiving a callback with the Policy object + Revision + AuditEventType'}, 'callback_revision_table_hash': {'type': 'string', 'format': '', 'example': '', 'description': 'A URL receiving a callback with <string> + AuditEventType. Periodically, the system can publish the hash of the revision table.'}, 'callback_signature_table_hash': {'type': 'string', 'format': '', 'example': '', 'description': 'A URL receiving a callback with <string> + AuditEventType. Periodically, the system can publish the hash of the signature table.'}}}, 'AuditEventType': {'type': 'object', 'description': 'TBD: Model for the possible events pertaining a change to an object subject to auditing. This model is not necessarily a database-backed model, but part of application code.', 'required': ['id', 'event_name'], 'properties': {'id': {'type': 'string', 'format': '', 'example': '', 'description': ''}, 'event_name': {'type': 'string', 'format': '', 'example': '', 'description': 'What happened - create/update/delete'}}}, 'StatusStartup': {'type': 'object', 'description': 'This model is not stored in a database. It describes the status of the Building Block while starting up. API should not be public. This call is blocking until the system is ready, a timeout occurs or an error is detected.', 'required': ['status', 'error_message', 'waiting_for'], 'properties': {'status': {'type': 'string', 'format': '', 'example': '', 'description': 'Possible values: OK, TIMEOUT, ERROR'}, 'error_message': {'type': 'string', 'format': '', 'example': '', 'description': 'Description of failure'}, 'waiting_for': {'type': 'string', 'format': '', 'example': '', 'description': 'When a timeout occurs, a list of pending operations may be shared'}}}, 'StatusReadiness': {'type': 'object', 'description': 'This model is not stored in a database. It describes the status of the Building Block while running. Returns immediately. API should not be public.', 'required': ['status', 'error_message', 'waiting_for'], 'properties': {'status': {'type': 'string', 'format': '', 'example': '', 'description': 'Possible values: OK, WAITING, ERROR'}, 'error_message': {'type': 'string', 'format': '', 'example': '', 'description': 'Description of failure'}, 'waiting_for': {'type': 'string', 'format': '', 'example': '', 'description': 'When a timeout occurs, a list of pending operations may be shared'}}}}, 'securitySchemes': {'OAuth2': {'type': 'oauth2', 'flows': {'authorizationCode': {'authorizationUrl': 'https://example.com/oauth/authorize', 'tokenUrl': 'https://example.com/oauth/token', 'scopes': {'read': 'Grants global read access', 'write': 'Grants global write access', 'org': 'Grants access to org operations', 'consumer': 'Grants access to data consumer operations', 'individual': 'Grants access to specific individual read/write operations', 'auditor': 'Grants access to specific auditor read operations'}}}}}}, 'security': [{'OAuth2': ['read']}]}

from django.db import models


class Individual(models.Model):
    """Shallowly models an Individual which may reference some instance in an external system (registration system, functional ID, foundational ID etc). An Individual instance of this model is not to be mistaken with a unique natural individual. It is up to the system owner to decide if this record permits mapping to a natural individual and/or if a single Individual row can map to several consent agreements."""
    
    external_id = models.CharField(
        verbose_name="external_id",
        help_text="Reference to another foundational/functional ID, which is likely PII",
        max_length=1024,
    )

    external_id_type = models.CharField(
        verbose_name="external_id_type",
        help_text="External id type specifier. A string. For instance \"email\" or \"foundational id\". Can be used in later queries.",
        max_length=1024,
    )

    identity_provider_id = models.CharField(
        verbose_name="identity_provider_id",
        help_text="This could be an FK, but for now we do not have a mapping of identity providers. IDBB may have more requirements.",
        max_length=1024,
    )


class Agreement(models.Model):
    """An agreement contains the specification of a single purpose that can be consented to. An Agreement is universal and can be consented to by *many* individuals through a ConsentRecord"""
    
    version = models.CharField(
        verbose_name="version",
        help_text="The version of this specification to which a receipt conforms",
        max_length=1024,
    )

    controller = models.ForeignKey(
        "Controller",
        verbose_name="controller",
        help_text="Data controller (may be omitted if no data involved)",
        on_delete=models.PROTECT,
    )

    policy = models.ForeignKey(
        "Policy",
        verbose_name="policy",
        help_text="Reference to the policy under which this Agreement shall be governed",
        on_delete=models.PROTECT,
    )

    purpose = models.ForeignKey(
        "AgreementPurpose",
        verbose_name="purpose",
        help_text="Purpose of data processing or purpose of consent. Displayed to the user.",
        on_delete=models.PROTECT,
    )

    lawful_basis = models.CharField(
        verbose_name="lawful_basis",
        help_text="Lawful basis of the agreement - consent / legal_obligation / contract / vital_interest / public_task / legitimate_interest",
        max_length=1024,
    )

    data_use = models.CharField(
        verbose_name="data_use",
        help_text="null/data-source/data-using-service",
        max_length=1024,
    )

    dpia = models.CharField(
        verbose_name="dpia",
        help_text="Data Protection Impact Assessment",
        max_length=1024,
    )

    lifecycle = models.ForeignKey(
        "AgreementLifecycle",
        verbose_name="lifecycle",
        help_text="Current Lifecycle state of the Agreement",
        on_delete=models.PROTECT,
    )

    signature = models.ForeignKey(
        "Signature",
        verbose_name="signature",
        help_text="Signature of authorizing party of Agreement. Note: Signatures may be chained in case of multiple signatures.",
        on_delete=models.PROTECT,
    )

    active = models.BooleanField(
        verbose_name="active",
        help_text="Agreement is active and new ConsentRecords can be created.",
    )

    forgettable = models.BooleanField(
        verbose_name="forgettable",
        help_text="Consent Record may be deleted when consent is withdrawn, as its existence is not necessary for auditability.",
    )


class AgreementData(models.Model):
    """Agreement data contains specifications of exactly what is collected."""
    
    agreement = models.ForeignKey(
        "Agreement",
        verbose_name="agreement",
        help_text="",
        on_delete=models.PROTECT,
    )

    name = models.CharField(
        verbose_name="name",
        help_text="Name of the attribute, for instance \"name\" or \"age\"",
        max_length=1024,
    )

    sensitivity = models.CharField(
        verbose_name="sensitivity",
        help_text="categories of sensitivity",
        max_length=1024,
    )

    category = models.CharField(
        verbose_name="category",
        help_text="",
        max_length=1024,
    )

    hash = models.CharField(
        verbose_name="hash",
        help_text="In order to sign an Agreement, this relation needs to have a cryptopgraphic hash to be included in the Signature of the Agreement.",
        max_length=1024,
    )


class Policy(models.Model):
    """A policy governs data and Agreement in the realm of an organisation that is refered to as \"data controller\" (GDPR) and owner of referencing Agreements."""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of the policy",
        max_length=1024,
    )

    version = models.CharField(
        verbose_name="version",
        help_text="Version of the policy",
        max_length=1024,
    )

    url = models.CharField(
        verbose_name="url",
        help_text="Permanent URL at which this very version of the Policy can be read, should not be allowed to change over time.",
        max_length=1024,
    )

    jurisdiction = models.CharField(
        verbose_name="jurisdiction",
        help_text="",
        max_length=1024,
    )

    industry_sector = models.CharField(
        verbose_name="industry_sector",
        help_text="",
        max_length=1024,
    )

    data_retention_period_days = models.IntegerField(
        verbose_name="data_retention_period_days",
        help_text="",
    )

    geographic_restriction = models.CharField(
        verbose_name="geographic_restriction",
        help_text="",
        max_length=1024,
    )

    storage_location = models.CharField(
        verbose_name="storage_location",
        help_text="",
        max_length=1024,
    )


class ConsentRecord(models.Model):
    """A Consent Record expresses consent (as defined in this building block's specification) to a single Agreement. There must be a UNIQUE constraint on (agreement_revision, individual)"""
    
    agreement = models.ForeignKey(
        "Agreement",
        verbose_name="agreement",
        help_text="The Agreement to which consent has been given",
        on_delete=models.PROTECT,
    )

    agreement_revision = models.ForeignKey(
        "Revision",
        verbose_name="agreement_revision",
        help_text="The Revision of the agreement which consent has been given to",
        on_delete=models.PROTECT,
    )

    individual = models.ForeignKey(
        "Individual",
        verbose_name="individual",
        help_text="The Individual who has signed this consent record",
        on_delete=models.PROTECT,
    )

    opt_in = models.BooleanField(
        verbose_name="opt_in",
        help_text="True: The individual has positively opted in. False: The individual has explicitly said no (or withdrawn a previous consent).",
    )

    state = models.CharField(
        verbose_name="state",
        help_text="The state field is used to record state changes after-the-fact. It is maintained by the Consent BB itself. Valid states: unsigned/pending more signatures/signed",
        max_length=1024,
    )

    signature = models.ForeignKey(
        "Signature",
        verbose_name="signature",
        help_text="A signature that hashes all the values of the consent record and has signed it with the key of the Invidiual, making it verifiable and tamper-proof. TBD: Relation to a Signature schema?",
        on_delete=models.PROTECT,
    )


class Revision(models.Model):
    """A *generic* revision model captures the serialized contents of any shema's single row. This is then subject to 1) cryptographic signature and 2) auditing.\n\nAside from \"successor\" column, a revision should be considered locked."""
    
    schema = models.CharField(
        verbose_name="schema",
        help_text="",
        max_length=1024,
    )

    object_id = models.CharField(
        verbose_name="object_id",
        help_text="",
        max_length=1024,
    )

    serialized_snapshot = models.CharField(
        verbose_name="serialized_snapshot",
        help_text="",
        max_length=1024,
    )

    timestamp = models.CharField(
        verbose_name="timestamp",
        help_text="",
        max_length=1024,
    )

    authorized_by_individual = models.ForeignKey(
        "Individual",
        verbose_name="authorized_by_individual",
        help_text="",
        on_delete=models.PROTECT,
    )

    authorized_by_other = models.CharField(
        verbose_name="authorized_by_other",
        help_text="Reference to an admin user that has created this revision",
        max_length=1024,
    )

    successor = models.ForeignKey(
        "Revision",
        verbose_name="successor",
        help_text="This revision is no longer the latest revision, refer to its successor.",
        on_delete=models.PROTECT,
    )

    predecessor_hash = models.CharField(
        verbose_name="predecessor_hash",
        help_text="Tamper-resistent artifact from previous record",
        max_length=1024,
    )

    predecessor_signature = models.CharField(
        verbose_name="predecessor_signature",
        help_text="Tamper-resistent artifact from previous record (we don't know if the previous record was signed or not)",
        max_length=1024,
    )


class AgreementFilter(models.Model):
    """Query filter for API endpoint listing Agreement objects"""
    
    name = models.CharField(
        verbose_name="name",
        help_text="",
        max_length=1024,
    )


class ConsentRecordFilter(models.Model):
    """Query filter for API endpoint listing ConsentRecord objects"""
    
    opt_in = models.BooleanField(
        verbose_name="opt_in",
        help_text="",
    )

    agreement = models.ForeignKey(
        "Agreement",
        verbose_name="agreement",
        help_text="",
        on_delete=models.PROTECT,
    )

    agreement_revision = models.ForeignKey(
        "Revision",
        verbose_name="agreement_revision",
        help_text="",
        on_delete=models.PROTECT,
    )

    individual = models.ForeignKey(
        "Individual",
        verbose_name="individual",
        help_text="",
        on_delete=models.PROTECT,
    )

    functional_id = models.CharField(
        verbose_name="functional_id",
        help_text="",
        max_length=1024,
    )

    foundational_id = models.CharField(
        verbose_name="foundational_id",
        help_text="",
        max_length=1024,
    )


class PolicyFilter(models.Model):
    """Query filter for API endpoint listing Policy objects"""
    
    name = models.CharField(
        verbose_name="name",
        help_text="",
        max_length=1024,
    )

    revision = models.ForeignKey(
        "Revision",
        verbose_name="revision",
        help_text="",
        on_delete=models.PROTECT,
    )


class Controller(models.Model):
    """Details of a data controller."""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of data controller (may be omitted if no data involved)",
        max_length=1024,
    )

    url = models.CharField(
        verbose_name="url",
        help_text="URL of data controller (may be omitted if no data involved)",
        max_length=1024,
    )


class Signature(models.Model):
    """A generic signature contains a cryptographic hash of some value, together with a signature created by some private key in another system. Required signing methods: Revision object or another Signature object."""
    
    payload = models.CharField(
        verbose_name="payload",
        help_text="The payload that is signed, constructed as a serialization of fields verification_method + verification_hash + verification_artifact + verification_signed_by + verification_jws_header. Serialized as a JSON dict.",
        max_length=1024,
    )

    signature = models.CharField(
        verbose_name="signature",
        help_text="Signature (of payload), the format of the signature should be specified by either verification_method or verification_jws_header",
        max_length=1024,
    )

    verification_method = models.CharField(
        verbose_name="verification_method",
        help_text="A well-known string denoting which method is used. Valid values: <TBD>. We might expand this with a relation to which verification methods that are supported. There may be a minimal set of supported methods necessary.",
        max_length=1024,
    )

    verification_hash = models.CharField(
        verbose_name="verification_hash",
        help_text="Internally generated cryptographic hash of the value to be signed. The hash is (re)produced from the object_type and object_reference - but from the serialized data of those.",
        max_length=1024,
    )

    verification_artifact = models.CharField(
        verbose_name="verification_artifact",
        help_text="A verification artifact in the form of a scanned object, image, signature etc.",
        max_length=1024,
    )

    verification_signed_by = models.CharField(
        verbose_name="verification_signed_by",
        help_text="Because an identifier's information may change over time, there is a need to store that information at the time of signing. In case of a cryptographic signature, this field should contain some identifier for looking up or verifying the public key of the signing party. In case of a non-cryptographic signature, this field could contain a natural individual's names, personal number, email addresses - store a snapshot that binds to the signature at the time of signing. In case of a cryptographic signature, this may be the fingerprint of the individual's public key or in some cases, a token from the user's ID session.",
        max_length=1024,
    )

    verification_jws_header = models.CharField(
        verbose_name="verification_jws_header",
        help_text="Alternative to the verification_method, verification_hash and verification_signature, give a JWS serialized object (RFC7515)",
        max_length=1024,
    )

    timestamp = models.CharField(
        verbose_name="timestamp",
        help_text="Timestamp of signature, currently this field isn't part of the payload so it's not tamper-proof.",
        max_length=1024,
    )

    object_type = models.CharField(
        verbose_name="object_type",
        help_text="Name of the schema model that object_reference points to. Values: \"signature\" or \"revision\"",
        max_length=1024,
    )

    object_reference = models.CharField(
        verbose_name="object_reference",
        help_text="A symmetric relation / back reference to the object_type that was signed. We are currently just modelling signing another signature (a chain) or signing a Revision (which can be a revision of a consent record, an agreement, policy etc)",
        max_length=1024,
    )


class AgreementPurpose(models.Model):
    """TBD: Models the purpose of an agreement"""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of purpose",
        max_length=1024,
    )

    description = models.CharField(
        verbose_name="description",
        help_text="Description of purpose",
        max_length=1024,
    )

    hash = models.CharField(
        verbose_name="hash",
        help_text="In order to sign an Agreement, this relation needs to have a cryptopgraphic hash to be included in the Signature of the Agreement.",
        max_length=1024,
    )


class AgreementLifecycle(models.Model):
    """TBD: Models the valid lifecycle states of an Agreement"""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Definition / Preparation / Capture / Use / Proof",
        max_length=1024,
    )


class RegistryReference(models.Model):
    """TBD: When creating an Invidiual, we need some input that refers to a functional or foundational ID in an external system"""
    
    foundational_id = models.CharField(
        verbose_name="foundational_id",
        help_text="",
        max_length=1024,
    )

    functional_id = models.CharField(
        verbose_name="functional_id",
        help_text="",
        max_length=1024,
    )


class AuditTracker(models.Model):
    """TBD: An external tracker receiving information from the system that can be subject to external auditing and verification of correct behavior. This is one of several notification/monitor/subscription patterns that may be more suitable for an encrypted Pub/Sub service."""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of the auditing system",
        max_length=1024,
    )

    public_key = models.CharField(
        verbose_name="public_key",
        help_text="The auditing system's public key for encrypting data sent to callback functions",
        max_length=1024,
    )

    callback_agreement = models.CharField(
        verbose_name="callback_agreement",
        help_text="A URL receiving a callback with the Agreement object + Revision + AuditEventType",
        max_length=1024,
    )

    callback_consent_record = models.CharField(
        verbose_name="callback_consent_record",
        help_text="A URL receiving a callback with the ConsentRecord object + Revision + AuditEventType",
        max_length=1024,
    )

    callback_policy = models.CharField(
        verbose_name="callback_policy",
        help_text="A URL receiving a callback with the Policy object + Revision + AuditEventType",
        max_length=1024,
    )

    callback_revision_table_hash = models.CharField(
        verbose_name="callback_revision_table_hash",
        help_text="A URL receiving a callback with <string> + AuditEventType. Periodically, the system can publish the hash of the revision table.",
        max_length=1024,
    )

    callback_signature_table_hash = models.CharField(
        verbose_name="callback_signature_table_hash",
        help_text="A URL receiving a callback with <string> + AuditEventType. Periodically, the system can publish the hash of the signature table.",
        max_length=1024,
    )


class AuditEventType(models.Model):
    """TBD: Model for the possible events pertaining a change to an object subject to auditing. This model is not necessarily a database-backed model, but part of application code."""
    
    event_name = models.CharField(
        verbose_name="event_name",
        help_text="What happened - create/update/delete",
        max_length=1024,
    )


class StatusStartup(models.Model):
    """This model is not stored in a database. It describes the status of the Building Block while starting up. API should not be public. This call is blocking until the system is ready, a timeout occurs or an error is detected."""
    
    status = models.CharField(
        verbose_name="status",
        help_text="Possible values: OK, TIMEOUT, ERROR",
        max_length=1024,
    )

    error_message = models.CharField(
        verbose_name="error_message",
        help_text="Description of failure",
        max_length=1024,
    )

    waiting_for = models.CharField(
        verbose_name="waiting_for",
        help_text="When a timeout occurs, a list of pending operations may be shared",
        max_length=1024,
    )


class StatusReadiness(models.Model):
    """This model is not stored in a database. It describes the status of the Building Block while running. Returns immediately. API should not be public."""
    
    status = models.CharField(
        verbose_name="status",
        help_text="Possible values: OK, WAITING, ERROR",
        max_length=1024,
    )

    error_message = models.CharField(
        verbose_name="error_message",
        help_text="Description of failure",
        max_length=1024,
    )

    waiting_for = models.CharField(
        verbose_name="waiting_for",
        help_text="When a timeout occurs, a list of pending operations may be shared",
        max_length=1024,
    )



