---
description: This section provides context for this Building Block.
---

# 2 Description

The Consent Building Block enables services for individuals to approve the use of their personal data by defining the principles, functions, and architecture of an information system. For organisations that process personal data​,​ it provides the ability to know the ​individual's will and legitimately process such personal data. The Consent Building Block is a process-oriented GovStack Building Block facilitating auditable bilateral agreements within a multi-agent environment that integrates with most other Building Blocks.

This specification has used several available and recognised open standards below and legal frameworks (such as the [GDPR](https://gdpr.eu/)) for laying the groundwork for its approach to consent management.

* [Kantara Initiative](https://kantarainitiative.org/download/7902/) - Consent Specification
* [ISO 29184: 2020](https://www.iso.org/standard/70331.html): Online Privacy Notices and Consent
* [ISO/IEC 29100:2011](https://www.iso.org/standard/45123.html): Privacy Framework
* [ISO/TS 17975:2015](https://www.iso.org/standard/61186.html) Health informatics — Principles and data requirements for consent in the Collection, Use or Disclosure of personal health information
* [ISO/IEC TS 27560](https://www.iso.org/standard/80392.html) — Consent record information structure (under development)

## What Consent Is

In the GovStack context, consent is understood as a voluntary declaration by an individual to approve the processing of their Personal data. It is one specific justification for personal data processing that is assumed to be required by legal or ethical conditions. It assumes that the person can decide on processing their personal data, managed in and by other GovStack Building Blocks, and also that the person is free to withdraw their consent at any time.

Some examples of such consent are:

* allowing a healthcare provider to fetch socio-demographic data from a government-run population registry to provide adequate primary healthcare services.
* allowing a government official to fetch relevant data from other/multiple government-run registries to analyse the eligibility for a social benefit programme.
* allow a government official to send personal data to a bank for cash transfers on behalf of the government.

## What Consent Is Not

The use of consent should be avoided in cases as below, which are not part of this specification:

* When a person is simply informed of the processing of the data by the organisation as part of the service provided under contract or by an authority.
* When consent does not have to be obtained in a situation where the entity does not identify or cannot identify people with reasonable effort.

## Assumptions

Lays out the pre-conditions needed for anyone to use the Consent Building Block.

1. Data Disclosure Agreements between organisations are already in place. For example, a healthcare organisation has already got the required authorisation to use the citizen data registry.
2. To link a Consent Agreement with the specific Individual, Consent Building Block assumes the authentication and authorization to be handled in a trusted manner outside of it (see below).
3. Within the early scope of the Consent Building Block, the act of delegating is kept outside the scope of the Consent Building Block. It is assumed that the authorisation to act on behalf of someone else is already resolved.
4. It is the organization's (a Data Provider or a Data Consumer) obligation to manage and implement internal policies toward its employees relating to their responsibilities for Personal data processing integrity, specifying it in the employment contract or by other means.

## Consent Agreement Lifecycle

The life cycle of consent management starts and ends within the organisation responsible for the information system. The organisation knows the context in which the information system operates and the intended purpose of the service. The rules and regulations to be applied for a given level of assurance define the functional framework for consent management.

Consent Building Block deals with transparency on data usage in a given context. Thus privacy-by-design of the system's actors is often an excellent guiding principle for interpreting international, national, and organisational policies and governance principles to implement the functional consent framework. A tangible outcome from a Data Protection Impact Analysis (DPIA) is a structured approach that can deliver the input for the actual implementation of the Consent Building Block.

Individual consent is captured within the context of digital interaction. This interaction is composite of all the information systems involved, not solely the Consent Building Block. Thus, the legal and ethical boundaries of consent are defined in the entirety of the interaction. In particular, consent, as defined by ISO/TS 17975:2015(E), should be seen as a "set of agreements and constraints" that an informed and knowledgeable \[individual] agrees to apply to their data processing. This definition, not based on the purpose of the data usage, can lead to a consent management framework also incorporating authorisations or unrelated constraints of the system. For example, in health information and healthcare service delivery, consent is also the process whereby a set of constraints is agreed upon so that information may be collected and used or disclosed. However, it is also the outcome of the process. As a rule of thumb, limiting unintended secondary usage of data is helpful to separate "consent" for a purpose from "consent" as an agreement to constraints and authorisation imposed by the system's functional requirements.

As a result, the organisation responsible for the information system is the driver of the definition of the functional consent management framework. It is also the function of the organisation to design the workflow for obtaining and processing the consent in a way that is purposeful, but not annoying for individuals or data processors with unnecessary bureaucratic overhead. From this framework, the Consent Building Block achieves its purpose by employing Consent Agreements that contain the following:

* A data policy that could be reused across multiple consent agreements (for example, based on the General Data Protection Regulation or any specific regulation)
* The purpose of consent, processed data attributes
* Signatures

A consent agreement life-cycle has four main phases\[^2], as illustrated in the figure below:

<figure><img src=".gitbook/assets/Consent Workflow.png" alt=""><figcaption><p><a href="https://app.moqups.com/P01asyy7ba/view/page/a2cb2359e">Diagram Source</a></p></figcaption></figure>

**Definition**: In this phase, the organisation (a Data Provider or a Data Consumer) adopts and defines a Data Policy that applies to the industry or sector-specific data usage as a template. While this phase is considered a “black box” to the Consent Building Block, it is an essential reference point for configuration and compatibility checks in all following phases.

**Preparation**: In this phase, the organisation (Data Provider or Data Consumer) that intends to process personal data configures the Consent Agreement and relevant rules for its use. An organisation could use personal data for third-party data sharing, as an example.

**Capture**: In this phase, the Individual can review the Consent Agreement and, once agreed upon, it is captured in a Consent Record by the organisation and stored for verification. This allows an auditor to check and ensure records are in place to process the individual's personal data. In the future, this phase could also encompass delegation and other individual use cases.

**Proof**: In this phase, an organisation (A Data Provider or a Data Consumer) can demonstrate that a valid record exists for performing data processing within itself or with other organisations. This allows for internal usage and for an auditor to verify and ensure records are in place to process the individual's personal data.

## Actors

Consent Building Block enables interaction between three (3) distinct user categories, which in combination create the necessary trust framework for the integrity of personal data processing. The actors are defined via distinct human roles to be performed in various consent life-cycle phases:

1. Individual as the subject of personal data processing;
2. Administrator of the information system exchanging the personal data;
3. Data Processing Auditor maintaining independent oversight of the data processing.

Below is the graphical depiction of the actors and their interactions; a more detailed description of the Consent Building Block capabilities is provided in [Chapter 4 - Key Digital Functionalities](4-key-digital-functionalities.md).

<figure><img src="images/consent-bb-actors-02.png" alt=""><figcaption><p><a href="https://app.moqups.com/P01asyy7ba/view/page/ad64222d5">Diagram Source</a></p></figcaption></figure>

<figure><img src="images/consent-bb-actors-01.png" alt=""><figcaption><p><a href="https://app.moqups.com/P01asyy7ba/view/page/ad64222d5">Diagram Source</a></p></figcaption></figure>

It is important to realise that while the actors are defined via human roles, the consent-related interactions between such roles can be executed in machine-to-machine workflows performing tasks in the interest of the respective actor.

###

## Interactions with other Building Blocks

The overall relationship diagram is shown below.

![Diagram Source](images/consent-bb-relationships.png)

The table below summarises the key relationships consumed during a consent transaction.

| Building Block                      | Relationship description                                                                                                                                     |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Identity Building Block             | It is assumed the Consent Building Block has already obtained requisite access tokens.                                                                       |
| Digital Registries Building Block   | This is used to store any consent agreement, individual consent receipts etc.                                                                                |
| Workflow Building Block             | Manages the workflow and rules associated with requiring or not requiring consent to use personal data.                                                      |
| Scheduler Building Block            | Provides an engine for time-based triggers to various events of an automated business process, which might also require consent.                             |
| Information Mediator Building Block | The information mediator Building Block provides a gateway for exchanging data related to consenting workflows; it also provides logs for auditing purposes. |
