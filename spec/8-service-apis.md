---
description: >-
  This section provides a reference for APIs that should be implemented by this
  Building Block.
---

# 8 Service APIs

This section provides a reference for APIs that should be implemented by this Building Block. The APIs defined here establish a blueprint for how the Building Block will interact with other Building Blocks. Additional APIs may be implemented by the Building Block, but the listed APIs define a minimal set of functionality that should be provided by any implementation of this Building Block.

The [GovStack non-functional requirements document](https://govstack.gitbook.io/specification/v/1.0/architecture-and-nonfunctional-requirements/6-onboarding) provides additional information on how 'adaptors' may be used to translate an existing API to the patterns described here. This section also provides guidance on how candidate products are tested and how GovStack validates a product's API against the API specifications defined here.

The tests for the Consent Building Block can be found in [this GitHub repository](https://github.com/GovStackWorkingGroup/bb-consent/tree/main/test).

# 8.1 API specification

The following is an automated rendition of our latest [OpenAPI YAML specification](https://github.com/GovStackWorkingGroup/bb-consent/tree/1.1.0-rc1/api).


## 8.1.1 Config APIs

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/policy/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/policy/{policyId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/policy/{policyId}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/policy/{policyId}/" method="delete" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/policy/{policyId}/revisions/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/policies/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/data-agreement/{dataAgreementId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/data-agreement/{dataAgreementId}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/data-agreement/{dataAgreementId}/" method="delete" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/data-agreement/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/data-agreements/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/individual/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/individual/{individualId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/individuals/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/webhook/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/webhook/{webhookId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/webhook/{webhookId}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/webhook/{webhookId}/" method="delete" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/config/webhooks/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

## 8.1.2 Service APIs

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/{individualId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/{individualId}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individuals/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/data-agreement/{dataAgreementId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/policy/{policyId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/verification/data-agreements/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/verification/consentrecords/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/verification/consentrecord/{consentRecordId}" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/data-agreement/{dataAgreementId}/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/data-agreement/{dataAgreementId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/consent-record/draft/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/consent-record/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/consent-record/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/consent-record/{consentRecordId}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/consent-record/{consentRecordId}/signature/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/consent-record/{consentRecordId}/signature/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/data-agreement/{dataAgreementId}/all/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/service/individual/record/" method="delete" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

## 8.1.3 Audit APIs

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/audit/consentrecords/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/audit/consentrecord/{consentRecordId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/audit/data-agreements/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml" path="/audit/data-agreement/{dataAgreementId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/1.1.0-rc1/api/consent-openapi.yaml)
{% endswagger %}
None

