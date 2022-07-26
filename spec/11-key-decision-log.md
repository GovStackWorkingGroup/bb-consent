# 11 Key Decision Log

<!--
{% hint style="info" %}
Record a list of key decisons made in the Building Block project so that new contributors can understand the context of the content.
{% endhint %}
-->

<table>
  <tr>
   <td>
<strong>Date</strong>
   </td>
   <td><strong>Decision</strong>
   </td>
  </tr>
  <tr>
   <td>November-2021
   </td>
   <td>Decided to scope and work on basic flows first with Consent BB version 1.0. This will scope out some items as described in chapter <a href="#bookmark=id.bq9xib12o320">Out-of-scope and future enhancements</a>
   </td>
  </tr>
  <tr>
   <td>January-2022
   </td>
   <td>Removed “consenter” and “consentee” terminology: Due to the ambiguity of what these two terms mean, we strictly mention only “individual”, “data processor” and “data controller”.
   </td>
  </tr>
  <tr>
   <td>March-2022
   </td>
   <td>The lifecycle of a single Agreement should match a single purpose. A Consent Record can only match 1 Agreement.
   </td>
  </tr>
  <tr>
   <td>March-2022
   </td>
   <td>Data structures, API URL call structures etc., should never reveal personally identifiable information (PII). We assume that anonymised IDs and tokens can handle relations to identity.
   </td>
  </tr>
  <tr>
   <td>March-2022
   </td>
   <td>Right To Be Forgotten: The scope of this action is decided to be framed by each Agreement. The building block definition covers a variety of different use cases deleted to remove traces or needs to be retained is not by design necessary for the Consent BB to decide.
   </td>
  </tr>
  <tr>
   <td>March-2022
   </td>
   <td>Revision+Signature models are designed to give a tamper-resistant, auditable track of all schemas. Auditability means: 1) Event-based external tracking that may verify that the system’s data isn’t tampered with and 2) Revision and Signature logs that can be queried to periodically verify that specific event (such as data transactions) is happening in accordance with valid Consent Records and Agreements.
   </td>
  </tr>
</table>