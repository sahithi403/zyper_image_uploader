## Deploy And Scale

Heroku instances can be used to host the Django application including celery workers with a Redis backend. The celery
worker is meant for running the asynchronous thumbnail creation task.

In the current project, the images (original and thumbnails) are stored under Django temporary file storage. In the
final deploy, the files can instead be stored on AWS using Django's S3Boto3Storage backend.

To scale the application for large number of loads (1000x), here are a few possible optimizations. In the current
setup, a thumbnail creation task is triggered upon each image upload. Alternatively, one could write a periodic task
that queries for all images that don't yet have thumbnails generated and creates them accordingly. Another possible
optimization, if the use case permits, is to cache the API results. This would reduce the number of database lookups
significantly and would allow the application to scale well for higher network loads.