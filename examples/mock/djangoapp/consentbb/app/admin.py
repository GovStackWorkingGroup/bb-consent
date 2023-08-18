
# !!! This code is auto-generated, please do not modify
import json
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter

from django.core import serializers
from django.contrib import admin
from django.utils.safestring import mark_safe


from . import models


class BaseGovstackAdmin(admin.ModelAdmin):
    readonly_fields = ('data_prettified',)

    def data_prettified(self, instance):
        """Function to display pretty version of our data"""

        # Convert the data to sorted, indented JSON
        response = serializers.serialize('json', [instance, ], indent=2)
        
        # Strip the list
        json_dict = json.loads(response)
        response = json.dumps(json_dict[0], indent=2)
        
        # Just use the first object
        response = response

        # Get the Pygments formatter
        formatter = HtmlFormatter(style='colorful')

        # Highlight the data
        response = highlight(response, JsonLexer(), formatter)

        # Get the stylesheet
        style = "<style>" + formatter.get_style_defs() + "</style><br>"

        # Safe the output
        return mark_safe(style + response)

    data_prettified.short_description = 'Object as JSON'


@admin.register(models.Individual)
class IndividualAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Agreement)
class AgreementAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AgreementData)
class AgreementDataAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Policy)
class PolicyAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.ConsentRecord)
class ConsentRecordAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Revision)
class RevisionAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Controller)
class ControllerAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.Signature)
class SignatureAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AgreementPurpose)
class AgreementPurposeAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AgreementLifecycle)
class AgreementLifecycleAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.RegistryReference)
class RegistryReferenceAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AuditTracker)
class AuditTrackerAdmin(BaseGovstackAdmin):
    pass


@admin.register(models.AuditEventType)
class AuditEventTypeAdmin(BaseGovstackAdmin):
    pass



