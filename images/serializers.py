from rest_framework import serializers

from .models import Image
from .tasks import create_thumbnail


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"
        read_only_fields = ("thumbnail", "name")

    def create(self, validated_data):
        validated_data['name'] = validated_data['file'].name
        image = Image.objects.create(**validated_data)
        create_thumbnail.delay(image.id)
        return image
