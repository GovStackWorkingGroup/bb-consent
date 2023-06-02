# 8 Service APIs

The [GovStack non-functional requirements document](https://govstack.gitbook.io/specification/architecture-and-nonfunctional-requirements/6-onboarding) provides additional information on how 'adaptors' may be used to translate an existing API to the patterns described here. The following is an automated rendition of our latest [OpenAPI YAML specification](https://github.com/GovStackWorkingGroup/bb-consent/tree/main/api).

## 8.1 Configuration APIs

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/policy/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/policy/{policyId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/policy/{policyId}/revisions/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/policy/{id}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/policy/{id}/" method="delete" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/policies/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/agreement/{agreementId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/agreement/{agreementId}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/agreement/{agreementId}/" method="delete" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/agreement/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/config/agreements/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

## 8.2 Service APIs

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/{individualId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/{individualId}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/{individualId}/" method="delete" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individuals/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/agreement/{agreementId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/policy/{policyId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/purpose/{purposeId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/agreement/{agreementId}/agreementdata/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/verification/agreements/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/verification/agreement/{agreementId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/verification/consentrecords/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/record/agreement/{agreementId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/record/agreement/{agreementId}/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/record/consentrecord/draft/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/record/consentrecord/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/record/consentrecord/{consentRecordId}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/record/consentrecord/{consentRecordId}/signature/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/record/consentrecord/{consentRecordId}/signature/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/record/agreement/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/service/individual/record/" method="delete" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

## 8.3 Audit APIs

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/audit/trackers/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/audit/tracker/" method="post" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/audit/tracker/{trackerId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/audit/tracker/{trackerId}/" method="put" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/audit/tracker/{trackerId}/" method="delete" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/audit/consentrecords/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/audit/consentrecord/{consentRecordId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/audit/agreements/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/audit/agreement/{agreementId}/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

## 8.4 Status APIs

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/status/startup/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}

{% swagger src="https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml" path="/status/readiness/" method="get" %}
[https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml](https://raw.githubusercontent.com/GovStackWorkingGroup/bb-consent/main/api/consent-openapi.yaml)
{% endswagger %}
