
class Individual(models.Model):
    """Shallowly models an Individual which may reference some instance in an external system (registration system, functional ID, foundational ID etc). An Individual instance of this model is not to be mistaken with a unique natural individual. It is up to the system owner to decide if this record permits mapping to a natural individual and/or if a single Individual row can map to several consent agreements."""
    
    id = models.CharField(
        verbose_name="id",
        help_text="The unique ID of an Individual row.",
    )

    external_id = models.CharField(
        verbose_name="external_id",
        help_text="Reference to another foundational/functional ID, which is likely PII",
    )

    external_id_type = models.CharField(
        verbose_name="external_id_type",
        help_text="External id type specifier. A string. For instance "email" or "foundational id". Can be used in later queries.",
    )


class Agreement(models.Model):
    """An agreement contains the specification of a single purpose that can be consented to. An Agreement is universal and can be consented to by *many* individuals through a ConsentRecord"""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    version = models.CharField(
        verbose_name="version",
        help_text="The version of this specification to which a receipt conforms",
    )

    controller = models.ForeignKey(
        Controller,
        verbose_name="controller",
        help_text="Data controller (may be omitted if no data involved)",
    )

    policy = models.ForeignKey(
        Policy,
        verbose_name="policy",
        help_text="Reference to the policy under which this Agreement shall be governed",
    )

    purpose = models.ForeignKey(
        AgreementPurpose,
        verbose_name="purpose",
        help_text="Purpose of data processing or purpose of consent. Displayed to the user.",
    )

    lawful_basis = models.CharField(
        verbose_name="lawful_basis",
        help_text="Lawful basis of the agreement - consent / legal_obligation / contract / vital_interest / public_task / legitimate_interest",
    )

    data_use = models.CharField(
        verbose_name="data_use",
        help_text="null/data-source/data-using-service",
    )

    dpia = models.CharField(
        verbose_name="dpia",
        help_text="Data Protection Impact Assessment",
    )

    lifecycle = models.ForeignKey(
        AgreementLifecycle,
        verbose_name="lifecycle",
        help_text="Current Lifecycle state of the Agreement",
    )

    signature = models.ForeignKey(
        Signature,
        verbose_name="signature",
        help_text="Signature of authorizing party of Agreement. Note: Signatures may be chained in case of multiple signatures.",
    )

    active = models.BooleanField(
        verbose_name="active",
        help_text="Agreement is active and new ConsentRecords can be created.",
    )

    forgettable = models.BooleanField(
        verbose_name="forgettable",
        help_text="Agreement may be deleted when consent is withdrawn, as its existence is not necessary for auditability.",
    )


class AgreementData(models.Model):
    """Agreement data contains specifications of exactly what is collected."""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    agreement = models.ForeignKey(
        Agreement,
        verbose_name="agreement",
        help_text="",
    )

    name = models.CharField(
        verbose_name="name",
        help_text="Name of the attribute, for instance "name" or "age"",
    )

    sensitivity = models.CharField(
        verbose_name="sensitivity",
        help_text="TBD: categories of sensitivity from som ISO",
    )

    category = models.CharField(
        verbose_name="category",
        help_text="",
    )

    hash = models.CharField(
        verbose_name="hash",
        help_text="In order to sign an Agreement, this relation needs to have a cryptopgraphic hash to be included in the Signature of the Agreement.",
    )


class Policy(models.Model):
    """A policy governs data and Agreement in the realm of an organisation that is refered to as \"data controller\" (GDPR) and owner of referencing Agreements."""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    name = models.CharField(
        verbose_name="name",
        help_text="Name of the policy",
    )

    version = models.CharField(
        verbose_name="version",
        help_text="Version of the policy",
    )

    url = models.CharField(
        verbose_name="url",
        help_text="Permanent URL at which this very version of the Policy can be read, should not be allowed to change over time.",
    )

    jurisdiction = models.CharField(
        verbose_name="jurisdiction",
        help_text="",
    )

    industry_sector = models.CharField(
        verbose_name="industry_sector",
        help_text="",
    )

    data_retention_period_days = models.IntegerField(
        verbose_name="data_retention_period_days",
        help_text="",
    )

    geographic_restriction = models.CharField(
        verbose_name="geographic_restriction",
        help_text="",
    )

    storage_location = models.CharField(
        verbose_name="storage_location",
        help_text="",
    )


class ConsentRecord(models.Model):
    """A Consent Record expresses consent (as defined in this building block's specification) to a single Agreement. There must be a UNIQUE constraint on (agreement_revision, individual)"""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    agreement = models.ForeignKey(
        Agreement,
        verbose_name="agreement",
        help_text="The agreement to which consent has been given",
    )

    agreement_revision = models.ForeignKey(
        Revision,
        verbose_name="agreement_revision",
        help_text="",
    )

    individual = models.ForeignKey(
        Individual,
        verbose_name="individual",
        help_text="The individual who has signed this consent record",
    )

    opt_in = models.BooleanField(
        verbose_name="opt_in",
        help_text="True: The individual has positively opted in. False: The individual has explicitly said no (or withdrawn a previous consent).",
    )

    state = models.CharField(
        verbose_name="state",
        help_text="unsigned/pending more signatures/signed",
    )

    signature = models.ForeignKey(
        Signature,
        verbose_name="signature",
        help_text="A signature that hashes all the values of the consent record and has signed it with the key of the Invidiual, making it verifiable and tamper-proof. TBD: Relation to a Signature schema?",
    )


class Revision(models.Model):
    """A *generic* revision model captures the serialized contents of any shema's single row. This is then subject to 1) cryptographic signature and 2) auditing.\n\nAside from \"successor\" column, a revision should be considered locked."""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    schema = models.CharField(
        verbose_name="schema",
        help_text="",
    )

    object_id = models.CharField(
        verbose_name="object_id",
        help_text="",
    )

    serialized_snapshot = models.CharField(
        verbose_name="serialized_snapshot",
        help_text="",
    )

    timestamp = models.CharField(
        verbose_name="timestamp",
        help_text="",
    )

    authorized_by_individual = models.ForeignKey(
        Individual,
        verbose_name="authorized_by_individual",
        help_text="",
    )

    authorized_by_other = models.CharField(
        verbose_name="authorized_by_other",
        help_text="Reference to an admin user that has created this revision",
    )

    successor = models.ForeignKey(
        Revision,
        verbose_name="successor",
        help_text="This revision is no longer the latest revision, refer to its successor.",
    )

    predecessor_hash = models.CharField(
        verbose_name="predecessor_hash",
        help_text="Tamper-resistent artifact from previous record",
    )

    predecessor_signature = models.CharField(
        verbose_name="predecessor_signature",
        help_text="Tamper-resistent artifact from previous record (we don't know if the previous record was signed or not)",
    )


class AgreementFilter(models.Model):
    """Query filter for API endpoint listing Agreement objects"""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    name = models.CharField(
        verbose_name="name",
        help_text="",
    )


class ConsentRecordFilter(models.Model):
    """Query filter for API endpoint listing ConsentRecord objects"""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    opt_in = models.BooleanField(
        verbose_name="opt_in",
        help_text="",
    )

    agreement = models.ForeignKey(
        Agreement,
        verbose_name="agreement",
        help_text="",
    )

    agreement_revision = models.ForeignKey(
        Revision,
        verbose_name="agreement_revision",
        help_text="",
    )

    individual = models.ForeignKey(
        Individual,
        verbose_name="individual",
        help_text="",
    )

    functional_id = models.CharField(
        verbose_name="functional_id",
        help_text="",
    )

    foundational_id = models.CharField(
        verbose_name="foundational_id",
        help_text="",
    )


class PolicyFilter(models.Model):
    """Query filter for API endpoint listing Policy objects"""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    name = models.CharField(
        verbose_name="name",
        help_text="",
    )

    revision = models.ForeignKey(
        Revision,
        verbose_name="revision",
        help_text="",
    )


class Controller(models.Model):
    """Details of a data controller."""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    name = models.CharField(
        verbose_name="name",
        help_text="Name of data controller (may be omitted if no data involved)",
    )

    url = models.CharField(
        verbose_name="url",
        help_text="URL of data controller (may be omitted if no data involved)",
    )


class Signature(models.Model):
    """A generic signature contains a cryptographic hash of some value, together with a signature created by some private key in another system. Required signing methods: Revision object or another Signature object."""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    verification_method = models.CharField(
        verbose_name="verification_method",
        help_text="",
    )

    verification_hash = models.CharField(
        verbose_name="verification_hash",
        help_text="Internally generated cryptographic hash of the value to be signed.",
    )

    verification_signature = models.CharField(
        verbose_name="verification_signature",
        help_text="Signature of verification_hash",
    )

    verification_artifact = models.CharField(
        verbose_name="verification_artifact",
        help_text="A verification artifact in the form of a scanned object, image, signature etc.",
    )

    jws_header = models.CharField(
        verbose_name="jws_header",
        help_text="Alternative to the verification_method, verification_hash and verification_signature, give a JWS serialized object (RFC7515)",
    )

    signed_by = models.CharField(
        verbose_name="signed_by",
        help_text="Identifier information may change over time. This field could contain a natural individual's names, personal number, email addresses - store a snapshot that binds to the signature at the time of signing.",
    )

    timestamp = models.CharField(
        verbose_name="timestamp",
        help_text="Timestamp of signature",
    )

    object_type = models.CharField(
        verbose_name="object_type",
        help_text="signature/revision",
    )

    object_reference = models.CharField(
        verbose_name="object_reference",
        help_text="A symmetric relation / back reference to the object_type that was signed. We are currently just modelling signing another signature (a chain) or signing a Revision (which can be a revision of an agreement, policy etc)",
    )


class AgreementPurpose(models.Model):
    """TBD: Models the purpose of an agreement"""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    name = models.CharField(
        verbose_name="name",
        help_text="Name of purpose",
    )

    description = models.CharField(
        verbose_name="description",
        help_text="Description of purpose",
    )


class AgreementLifecycle(models.Model):
    """TBD: Models the valid lifecycle states of an Agreement"""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    name = models.CharField(
        verbose_name="name",
        help_text="Definition / Preparation / Capture / Use / Proof",
    )


class RegistryReference(models.Model):
    """TBD: When creating an Invidiual, we need some input that refers to a functional or foundational ID in an external system"""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    foundational_id = models.CharField(
        verbose_name="foundational_id",
        help_text="",
    )

    functional_id = models.CharField(
        verbose_name="functional_id",
        help_text="",
    )


class AuditTracker(models.Model):
    """TBD: An external tracker receiving information from the system that can be subject to external auditing and verification of correct behavior. This is one of several notification/monitor/subscription patterns that may be more suitable for an encrypted Pub/Sub service."""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    name = models.CharField(
        verbose_name="name",
        help_text="Name of the auditing system",
    )

    public_key = models.CharField(
        verbose_name="public_key",
        help_text="The auditing system's public key for encrypting data sent to callback functions",
    )

    callback_agreement = models.CharField(
        verbose_name="callback_agreement",
        help_text="A URL receiving a callback with the Agreement object + Revision + AuditEventType",
    )

    callback_consent_record = models.CharField(
        verbose_name="callback_consent_record",
        help_text="A URL receiving a callback with the ConsentRecord object + Revision + AuditEventType",
    )

    callback_policy = models.CharField(
        verbose_name="callback_policy",
        help_text="A URL receiving a callback with the Policy object + Revision + AuditEventType",
    )

    callback_revision_table_hash = models.CharField(
        verbose_name="callback_revision_table_hash",
        help_text="A URL receiving a callback with <string> + AuditEventType. Periodically, the system can publish the hash of the revision table.",
    )

    callback_signature_table_hash = models.CharField(
        verbose_name="callback_signature_table_hash",
        help_text="A URL receiving a callback with <string> + AuditEventType. Periodically, the system can publish the hash of the signature table.",
    )


class AuditEventType(models.Model):
    """TBD: Model for the possible events pertaining a change to an object subject to auditing. This model is not necessarily a database-backed model, but part of application code."""
    
    id = models.CharField(
        verbose_name="id",
        help_text="",
    )

    event_name = models.CharField(
        verbose_name="event_name",
        help_text="What happened - create/update/delete",
    )


