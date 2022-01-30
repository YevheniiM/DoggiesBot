from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    bucket_name = 'doggies-bot'
    location = 'files'


class StaticStorage(S3Boto3Storage):
    bucket_name = 'doggies-bot'
    location = 'static'


media_storage = MediaStorage()
