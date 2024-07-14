from django.apps import AppConfig
import os


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    def ready(self):
        if os.environ.get('RUN_MAIN') == 'True':
            from mailing.services import start_scheduler
            start_scheduler()
