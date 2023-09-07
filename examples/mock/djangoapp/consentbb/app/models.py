
# !!! This code is auto-generated, please do not modify

from django.db import models


class Individual(models.Model):
    """Shallowly models an Individual which may reference some instance in an external system (registration system, functional ID, foundational ID etc). An Individual instance of this model is not to be mistaken with a unique natural individual. It is up to the system owner to decide if this record permits mapping to a natural individual and/or if a single Individual row can map to several consent agreements."""
    
    external_id = models.CharField(
        verbose_name="external_id",
        help_text="Reference to another foundational/functional ID, which is likely PII",
        max_length=1024,
        null=True,
        blank=True,
    )

    external_id_type = models.CharField(
        verbose_name="external_id_type",
        help_text="External id type specifier. A string. For instance \"email\" or \"foundational id\". Can be used in later queries.",
        max_length=1024,
        null=True,
        blank=True,
    )

    identity_provider_id = models.CharField(
        verbose_name="identity_provider_id",
        help_text="This could be an FK, but for now we do not have a mapping of identity providers. IDBB may have more requirements.",
        max_length=1024,
        null=True,
        blank=True,
    )



class Agreement(models.Model):
    """An agreement contains the specification of a single purpose that can be consented to. An Agreement is universal and can be consented to by *many* individuals through a ConsentRecord"""
    
    version = models.CharField(
        verbose_name="version",
        help_text="The version of this specification to which a receipt conforms",
        max_length=1024,
        null=False,
        blank=False,
    )

    controller = models.ForeignKey(
        "Controller",
        verbose_name="controller",
        help_text="Data controller (may be omitted if no data involved)",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    policy = models.ForeignKey(
        "Policy",
        verbose_name="policy",
        help_text="Reference to the policy under which this Agreement shall be governed",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    purpose = models.ForeignKey(
        "AgreementPurpose",
        verbose_name="purpose",
        help_text="Purpose of data processing or purpose of consent. Displayed to the user.",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    lawful_basis = models.CharField(
        verbose_name="lawful_basis",
        help_text="Lawful basis of the agreement - consent / legal_obligation / contract / vital_interest / public_task / legitimate_interest",
        max_length=1024,
        null=False,
        blank=False,
    )

    data_use = models.CharField(
        verbose_name="data_use",
        help_text="null/data_source/data_using_service",
        max_length=1024,
        null=True,
        blank=True,
    )

    dpia = models.CharField(
        verbose_name="dpia",
        help_text="Data Protection Impact Assessment",
        max_length=1024,
        null=False,
        blank=False,
    )

    signature = models.ForeignKey(
        "Signature",
        verbose_name="signature",
        help_text="Signature of authorizing party of Agreement. Note: Signatures may be chained in case of multiple signatures.",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    active = models.BooleanField(
        verbose_name="active",
        help_text="Agreement is active and new ConsentRecords can be created.",
        null=True,
        blank=True,
    )

    forgettable = models.BooleanField(
        verbose_name="forgettable",
        help_text="Consent Record may be deleted when consent is withdrawn, as its existence is not necessary for auditability.",
        null=True,
        blank=True,
    )

    compatible_with_version = models.ForeignKey(
        "Agreement",
        verbose_name="compatible_with_version",
        help_text="WIP: This field indicates that Consent Records may be transferred from this compatible previous version of the same Agreement.",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    lifecycle = models.ForeignKey(
        "AgreementLifecycle",
        verbose_name="lifecycle",
        help_text="WIP: Current Lifecycle state of the Agreement. Lifecycle states are used to manage internal workflows and should not be assigned semantic meanings for active Consent Records.",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )



class AgreementData(models.Model):
    """Agreement data contains specifications of exactly what is collected."""
    
    agreement = models.ForeignKey(
        "Agreement",
        verbose_name="agreement",
        help_text="",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    name = models.CharField(
        verbose_name="name",
        help_text="Name of the attribute, for instance \"name\" or \"age\"",
        max_length=1024,
        null=False,
        blank=False,
    )

    sensitivity = models.CharField(
        verbose_name="sensitivity",
        help_text="categories of sensitivity",
        max_length=1024,
        null=False,
        blank=False,
    )

    category = models.CharField(
        verbose_name="category",
        help_text="",
        max_length=1024,
        null=False,
        blank=False,
    )

    serialized_hash = models.CharField(
        verbose_name="serialized_hash",
        help_text="In order to sign an Agreement, this relation needs to have a cryptopgraphic hash of the JSON serialized data to be included in the Signature payload of the Agreement. Hashes are collected as the hex representation of the SHA-1 sum of all UTF8 encoded string versions of the JSON representation of data. SHA1(json_serialized_data)",
        max_length=1024,
        null=False,
        blank=False,
    )



class Policy(models.Model):
    """A policy governs data and Agreement in the realm of an organisation that is refered to as \"data controller\" (GDPR) and owner of referencing Agreements."""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of the policy",
        max_length=1024,
        null=False,
        blank=False,
    )

    version = models.CharField(
        verbose_name="version",
        help_text="Version of the policy",
        max_length=1024,
        null=False,
        blank=False,
    )

    url = models.CharField(
        verbose_name="url",
        help_text="Permanent URL at which this very version of the Policy can be read, should not be allowed to change over time.",
        max_length=1024,
        null=False,
        blank=False,
    )

    jurisdiction = models.CharField(
        verbose_name="jurisdiction",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )

    industry_sector = models.CharField(
        verbose_name="industry_sector",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )

    data_retention_period_days = models.IntegerField(
        verbose_name="data_retention_period_days",
        help_text="",
        null=True,
        blank=True,
    )

    geographic_restriction = models.CharField(
        verbose_name="geographic_restriction",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )

    storage_location = models.CharField(
        verbose_name="storage_location",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )



class ConsentRecord(models.Model):
    """A Consent Record expresses consent (as defined in this building block's specification) to a single Agreement. There must be a UNIQUE constraint on (agreement_revision, individual)"""
    
    agreement = models.ForeignKey(
        "Agreement",
        verbose_name="agreement",
        help_text="The Agreement to which consent has been given",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    agreement_revision = models.ForeignKey(
        "Revision",
        verbose_name="agreement_revision",
        help_text="The Revision of the agreement which consent has been given to",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    individual = models.ForeignKey(
        "Individual",
        verbose_name="individual",
        help_text="The Individual who has signed this consent record",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    opt_in = models.BooleanField(
        verbose_name="opt_in",
        help_text="True: The individual has positively opted in. False: The individual has explicitly said no (or withdrawn a previous consent).",
        null=True,
        blank=True,
    )

    state = models.CharField(
        verbose_name="state",
        help_text="The state field is used to record state changes after-the-fact. It is maintained by the Consent BB itself. Valid states: unsigned/pending more signatures/signed",
        max_length=1024,
        null=False,
        blank=False,
    )

    signature = models.ForeignKey(
        "Signature",
        verbose_name="signature",
        help_text="A signature that hashes all the values of the consent record and has signed it with the key of the Invidiual, making it verifiable and tamper-proof. TBD: Relation to a Signature schema?",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )



class Revision(models.Model):
    """A *generic* revision model captures the serialized contents of any shema's single row. This is then subject to 1) cryptographic signature and 2) auditing.\n\nAside from \"successor\" column, a revision should be considered locked."""
    
    schema_name = models.CharField(
        verbose_name="schema_name",
        help_text="This was previously called \"schema\" but for technical reasons should be called \"schema_name\"",
        max_length=1024,
        null=False,
        blank=False,
    )

    object_id = models.CharField(
        verbose_name="object_id",
        help_text="The PK of the object that was serialized.",
        max_length=1024,
        null=False,
        blank=False,
    )

    serialized_snapshot = models.CharField(
        verbose_name="serialized_snapshot",
        help_text="Revisioned data (serialized as JSON)",
        max_length=1024,
        null=False,
        blank=False,
    )

    serialized_hash = models.CharField(
        verbose_name="serialized_hash",
        help_text="Hash of serialized_snapshot (SHA-1)",
        max_length=1024,
        null=False,
        blank=False,
    )

    timestamp = models.CharField(
        verbose_name="timestamp",
        help_text="Timestamp of when revisioning happened",
        max_length=1024,
        null=False,
        blank=False,
    )

    authorized_by_individual = models.ForeignKey(
        "Individual",
        verbose_name="authorized_by_individual",
        help_text="",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    authorized_by_other = models.CharField(
        verbose_name="authorized_by_other",
        help_text="Reference to an admin user that has created this revision",
        max_length=1024,
        null=True,
        blank=True,
    )

    successor = models.ForeignKey(
        "Revision",
        verbose_name="successor",
        help_text="This revision is no longer the latest revision, refer to its successor.",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    predecessor_hash = models.CharField(
        verbose_name="predecessor_hash",
        help_text="Tamper-resistent artifact from previous record, copied from serialized_hash",
        max_length=1024,
        null=True,
        blank=True,
    )

    predecessor_signature = models.CharField(
        verbose_name="predecessor_signature",
        help_text="Tamper-resistent artifact from previous record (we don't know if the previous record was signed or not)",
        max_length=1024,
        null=True,
        blank=True,
    )



class Controller(models.Model):
    """Details of a data controller."""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of data controller (may be omitted if no data involved)",
        max_length=1024,
        null=False,
        blank=False,
    )

    url = models.CharField(
        verbose_name="url",
        help_text="URL of data controller (may be omitted if no data involved)",
        max_length=1024,
        null=False,
        blank=False,
    )



class Signature(models.Model):
    """A generic signature contains a cryptographic hash of some value, together with a signature created by some private key in another system. Required signing methods: Revision object or another Signature object."""
    
    payload = models.CharField(
        verbose_name="payload",
        help_text="The payload that is signed, constructed as a serialization of fields verification_method + verification_hash + verification_artifact + verification_signed_by + verification_jws_header. Serialized as a JSON dict.",
        max_length=1024,
        null=False,
        blank=False,
    )

    signature = models.CharField(
        verbose_name="signature",
        help_text="Signature of payload hash, the format of the signature should be specified by either verification_method or verification_jws_header",
        max_length=1024,
        null=False,
        blank=False,
    )

    verification_method = models.CharField(
        verbose_name="verification_method",
        help_text="A well-known string denoting which method is used. Valid values: <TBD>. We might expand this with a relation to which verification methods that are supported. There may be a minimal set of supported methods necessary.",
        max_length=1024,
        null=False,
        blank=False,
    )

    verification_payload = models.CharField(
        verbose_name="verification_payload",
        help_text="Internally generated serialized version of the data referenced by object_type and object_reference - by extracting and serializing their data as JSON.",
        max_length=1024,
        null=False,
        blank=False,
    )

    verification_payload_hash = models.CharField(
        verbose_name="verification_payload_hash",
        help_text="Internally generated cryptographic hash of the value to be signed, i.e. the value of verification_payload",
        max_length=1024,
        null=False,
        blank=False,
    )

    verification_artifact = models.CharField(
        verbose_name="verification_artifact",
        help_text="A verification artifact in the form of a scanned object, image, signature etc.",
        max_length=1024,
        null=True,
        blank=True,
    )

    verification_signed_by = models.CharField(
        verbose_name="verification_signed_by",
        help_text="Because an identifier's information may change over time, there is a need to store that information at the time of signing. In case of a cryptographic signature, this field should contain some identifier for looking up or verifying the public key of the signing party. In case of a non-cryptographic signature, this field could contain a natural individual's names, personal number, email addresses - store a snapshot that binds to the signature at the time of signing. In case of a cryptographic signature, this may be the fingerprint of the individual's public key or in some cases, a token from the user's ID session.",
        max_length=1024,
        null=False,
        blank=False,
    )

    verification_signed_as = models.CharField(
        verbose_name="verification_signed_as",
        help_text="DRAFT FIELD: Specifies the relationship between the authorizing signature and the invidual which the payload concerns. This is relevant for Consent Records. Possible values: \"individual\" / \"delegate\"",
        max_length=1024,
        null=True,
        blank=True,
    )

    verification_jws_header = models.CharField(
        verbose_name="verification_jws_header",
        help_text="Alternative to the verification_method, verification_hash and verification_signature, give a JWS serialized object (RFC7515)",
        max_length=1024,
        null=True,
        blank=True,
    )

    timestamp = models.CharField(
        verbose_name="timestamp",
        help_text="Timestamp of signature, currently this field isn't part of the payload so it's not tamper-proof.",
        max_length=1024,
        null=False,
        blank=False,
    )

    object_type = models.CharField(
        verbose_name="object_type",
        help_text="Name of the schema model that object_reference points to. Values: \"signature\" or \"revision\"",
        max_length=1024,
        null=True,
        blank=True,
    )

    object_reference = models.CharField(
        verbose_name="object_reference",
        help_text="A symmetric relation / back reference to the object_type that was signed. We are currently just modelling signing another signature (a chain) or signing a Revision (which can be a revision of a consent record, an agreement, policy etc)",
        max_length=1024,
        null=True,
        blank=True,
    )



class AgreementPurpose(models.Model):
    """TBD: Models the purpose of an agreement"""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of purpose",
        max_length=1024,
        null=False,
        blank=False,
    )

    description = models.CharField(
        verbose_name="description",
        help_text="Description of purpose",
        max_length=1024,
        null=False,
        blank=False,
    )

    serialized_hash = models.CharField(
        verbose_name="serialized_hash",
        help_text="In order to sign an Agreement, this relation needs to have a cryptopgraphic hash of the JSON serialized data to be included in the Signature payload of the Agreement. Hashes are collected as the hex representation of the SHA-1 sum of all UTF8 encoded string versions of the JSON representation of data. SHA1(json_serialized_data)",
        max_length=1024,
        null=True,
        blank=True,
    )



class AgreementLifecycle(models.Model):
    """TBD: Models the valid lifecycle states of an Agreement"""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Draft / Complete",
        max_length=1024,
        null=False,
        blank=False,
    )



class RegistryReference(models.Model):
    """TBD: When creating an Invidiual, we need some input that refers to a functional or foundational ID in an external system"""
    
    foundational_id = models.CharField(
        verbose_name="foundational_id",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )

    functional_id = models.CharField(
        verbose_name="functional_id",
        help_text="",
        max_length=1024,
        null=True,
        blank=True,
    )



class AuditTracker(models.Model):
    """TBD: An external tracker receiving information from the system that can be subject to external auditing and verification of correct behavior. This is one of several notification/monitor/subscription patterns that may be more suitable for an encrypted Pub/Sub service."""
    
    name = models.CharField(
        verbose_name="name",
        help_text="Name of the auditing system",
        max_length=1024,
        null=False,
        blank=False,
    )

    public_key = models.CharField(
        verbose_name="public_key",
        help_text="The auditing system's public key for encrypting data sent to callback functions",
        max_length=1024,
        null=False,
        blank=False,
    )

    callback_agreement = models.CharField(
        verbose_name="callback_agreement",
        help_text="A URL receiving a callback with the Agreement object + Revision + AuditEventType",
        max_length=1024,
        null=False,
        blank=False,
    )

    callback_consent_record = models.CharField(
        verbose_name="callback_consent_record",
        help_text="A URL receiving a callback with the ConsentRecord object + Revision + AuditEventType",
        max_length=1024,
        null=False,
        blank=False,
    )

    callback_policy = models.CharField(
        verbose_name="callback_policy",
        help_text="A URL receiving a callback with the Policy object + Revision + AuditEventType",
        max_length=1024,
        null=False,
        blank=False,
    )

    callback_revision_table_hash = models.CharField(
        verbose_name="callback_revision_table_hash",
        help_text="A URL receiving a callback with <string> + AuditEventType. Periodically, the system can publish the hash of the revision table.",
        max_length=1024,
        null=True,
        blank=True,
    )

    callback_signature_table_hash = models.CharField(
        verbose_name="callback_signature_table_hash",
        help_text="A URL receiving a callback with <string> + AuditEventType. Periodically, the system can publish the hash of the signature table.",
        max_length=1024,
        null=True,
        blank=True,
    )



class AuditEventType(models.Model):
    """TBD: Model for the possible events pertaining a change to an object subject to auditing. This model is not necessarily a database-backed model, but part of application code."""
    
    event_name = models.CharField(
        verbose_name="event_name",
        help_text="What happened - create/update/delete",
        max_length=1024,
        null=False,
        blank=False,
    )




