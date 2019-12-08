from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from django.core.files.storage import FileSystemStorage
from .models import Image
import uuid


from .models import Image
from .serializers import ImageSerializer


class ImageUploadAPIViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.all()
