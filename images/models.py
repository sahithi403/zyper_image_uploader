from django.db import models

# Create your models here.
from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField()
    thumbnail = models.FileField(null=True, blank=True)
    thumbnail_created = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name}"
