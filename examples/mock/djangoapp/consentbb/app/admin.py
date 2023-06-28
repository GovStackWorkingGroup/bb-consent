
# !!! This code is auto-generated, please do not modify

from django.contrib import admin
from . import models


@admin.register(models.Individual)
class IndividualAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Agreement)
class AgreementAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AgreementData)
class AgreementDataAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Policy)
class PolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConsentRecord)
class ConsentRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Revision)
class RevisionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AgreementFilter)
class AgreementFilterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ConsentRecordFilter)
class ConsentRecordFilterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.PolicyFilter)
class PolicyFilterAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Controller)
class ControllerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Signature)
class SignatureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AgreementPurpose)
class AgreementPurposeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AgreementLifecycle)
class AgreementLifecycleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.RegistryReference)
class RegistryReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AuditTracker)
class AuditTrackerAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AuditEventType)
class AuditEventTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StatusStartup)
class StatusStartupAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StatusReadiness)
class StatusReadinessAdmin(admin.ModelAdmin):
    pass



