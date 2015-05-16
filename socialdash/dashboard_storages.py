from django.conf import settings
from django.utils.deconstruct import deconstructible
from storages.backends.s3boto import S3BotoStorage

@deconstructible
class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION


@deconstructible
class MediaStorage(S3BotoStorage):
        location = settings.MEDIAFILES_LOCATION
