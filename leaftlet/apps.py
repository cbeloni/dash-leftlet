from django.apps import AppConfig

class LeaftletConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leaftlet'

    def ready(self):
        from leaftlet.job import qualidade_ar_job
        qualidade_ar_job.start()
