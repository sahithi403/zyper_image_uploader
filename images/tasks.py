from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Image
from PIL import Image as PIL_Image, ImageOps
import os
from django.core.files.uploadedfile import InMemoryUploadedFile


@shared_task
def create_thumbnail(image_id):
    # from celery.contrib import rdb
    # rdb.set_trace()

    image = Image.objects.get(pk=image_id)
    size = 300, 300
    image_file = PIL_Image.open(image.file, 'r')
    image_path = image.file.path
    image_loc = os.path.dirname(image_path)
    thumb = ImageOps.fit(image_file, size, PIL_Image.ANTIALIAS)
    image_file_name, extension = os.path.splitext(image.file.name)

    thumb_path = os.path.join(image_loc, image_file_name + "_thumbnail.jpeg")
    thumb = thumb.convert("RGB")
    thumb.save(thumb_path, "JPEG")

    f = open(thumb_path, 'rb')
    f = InMemoryUploadedFile(f, 'media_file', image_file_name + "_thumbnail.jpeg", 'image/jpg',
                                     os.path.getsize(thumb_path), None)

    image.thumbnail = f
    image.thumbnail_created = True

    image.save()