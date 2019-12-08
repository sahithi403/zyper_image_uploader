from django.db import models

# Create your models here.
from django.db import models


class Image(models.Model):
    file = models.FileField()
    thumbnail = models.FileField(null=True, blank=True)
    thumbnail_created = models.BooleanField(default=False)
    # thumbnail = models.ForeignKey('Thumbnail', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name}"
