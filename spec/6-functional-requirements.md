# 6 Functional Requirements

<!--
{% hint style="success" %}
The functional requirements section lists the technical capabilities that this building block should have. These requirements should be sufficient to deliver all functionality that is listed in the Key Digital Functionalities section.

These functional requirements do not define specific APIs - they provide a list of information about functionality that must be implemented within the building block.

These requirements should be defined by subject-matter experts and don’t have to be highly technical in this section..
{% endhint %}
-->
The functional requirements section lists the technical capabilities that this building block should have. These requirements should be sufficient to deliver all functionality that is listed in the Key Digital Functionalities section. These functional requirements do not define specific APIs - they provide a list of information about functionality that must be implemented within the building block. These requirements should be defined by subject-matter experts and don’t have to be highly technical in this section.

## 6.1  Consent Agreement Configuration Requirements

<table>
  <tr>
   <td>
<strong>Name</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Optionality</strong>
   </td>
  </tr>
  <tr>
   <td>Create Consent Agreement
   </td>
   <td>It shall be possible to create a consent agreement, either based on an existing or new data policy template. Each consent agreement shall be under version control.
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>View Consent Agreement
   </td>
   <td>It shall be possible to view an existing consent agreement
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Update Consent Agreement
   </td>
   <td>It shall be possible to update an existing consent agreement.
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Terminate Consent Agreement
   </td>
   <td>It shall be  possible to terminate an existing consent agreement
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Revision history
   </td>
   <td>It shall be possible to capture and sign all changes to Consent Agreements, Consent Policies and Consent Records in tamper-proof Revisions
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Change notification subscription
   </td>
   <td>It shall be possible to subscribe to enable or disable a change notification towards users
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Change notification
   </td>
   <td>It shall be possible to trigger a change notification when there are changes done to an existing consent agreement
   </td>
   <td>MAY
   </td>
  </tr>
  <tr>
   <td>Logging
   </td>
   <td>The BB  shall log all administrative functions
   </td>
   <td>MUST
   </td>
  </tr>
</table>


## 6.2 Individual Consent Requirements

<table>
  <tr>
   <td>
<strong>Name</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Optionality</strong>
   </td>
  </tr>
  <tr>
   <td>View consent agreement
   </td>
   <td>It shall be possible to view the associated consent agreement if it exists
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Agree (Opt-in)
   </td>
   <td>It shall be possible to agree or opt-in or sign a consent agreement 
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Withdraw (Opt-out)
   </td>
   <td>It shall be possible to opt-out of a previously signed or agreed consent agreement
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Logging
   </td>
   <td>All individual consent actions shall be logged
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Change notification subscription
   </td>
   <td>It shall be possible to enable or disable consent change notification
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Change notification
   </td>
   <td>It shall be possible to trigger a consent agreement change notification towards individuals
   </td>
   <td>MAY
   </td>
  </tr>
</table>




 ## 6.3 Consent Audit Requirements

<table>
  <tr>
   <td>
<strong>Name</strong>
   </td>
   <td><strong>Description</strong>
   </td>
   <td><strong>Optionality</strong>
   </td>
  </tr>
  <tr>
   <td>Audit logging
   </td>
   <td>All consent logs shall be tamperproof
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>View and verify the consent agreement
   </td>
   <td>It shall be possible to view and verify a shared consent agreement
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>View and verify consents
   </td>
   <td>It shall be possible to view and verify a signed consent agreement
   </td>
   <td>MUST
   </td>
  </tr>
  <tr>
   <td>Revision list
   </td>
   <td>It shall be possible to filter and sort all objects’ revision histories can be filtered and sorted
   </td>
   <td>MUST
   </td>
  </tr>
</table>