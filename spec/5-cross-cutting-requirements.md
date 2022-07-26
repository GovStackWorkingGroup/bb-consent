# 5 Cross-Cutting Requirements
<!--
{% hint style="success" %}
The Cross-cutting requirements described in this section are an extension of the cross-cutting requirements defined in the architecture blueprint and nonfunctional requirements document. This section will describe any additional cross-cutting requirements that apply to this building block.

Cross-cutting requirements will use the same language (MUST or SHOULD) as specified in the architecture document.
{% endhint %}
-->

The Cross-cutting requirements described in this section are an extension of the cross-cutting requirements defined in the architecture specification document. This section will describe any additional cross-cutting requirements for this building block.

Cross-cutting requirements will use the same language (MUST or SHOULD) as specified in the architecture document.

<table>
  <tr>
   <td>Digital Registries BB
   </td>
   <td>Must provide all functions related to the persistent storage of consent data. 
   </td>
  </tr>
  <tr>
   <td>Information Mediator BB
   </td>
   <td>Shall provide functions to register Data Providers from which the Data Consumer will fetch the data.
   </td>
  </tr>
</table>

## 5.1 Privacy

Personal data MUST be kept private and never shared with any parties, except where specific authorisation has been granted. The Consent BB shall follow the privacy principles as laid out in the Govstack architecture. 

## 5.2  Data Policy Audit Logging 

Logs MUST be kept in a database of all created, updated, or deleted records. Logs MUST include timestamps and identify the user and affiliation that performed the transaction. 

All audit logs shall be integrity protected against tampering. The Consent BB shall follow the data policy and audit logging requirements as laid out in the Govstack architecture.

## 5.3  Source Code and Licensing

A GovStack Building Block MUST be Open-source Only with No Vendor Lock-in.

## 5.4 Security Requirements

In general, the Consent BB shall follow the security requirements as laid out in the Govstack architecture. Consent BB’s API endpoints are invoked with a client-supplied API key which MUST defer to the Identification and Verification BB in order to verify the role and/or scope of the API key matches the API endpoint to which it is supplied. This is mentioned here, as this Definition is drafted without clear guidance in the OpenAPI spec for the handling of roles and scopes. 

MUST adhere to all requirements from[ Security BB requirements.](https://www.govstack.global/wp-content/uploads/2021/08/Security_Building_Block_Definition_1.0.1.pdf)
