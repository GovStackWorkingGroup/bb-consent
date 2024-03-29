from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consentbb.app'
    label = 'app'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals
