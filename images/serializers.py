from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"
        read_only_fields = ("thumbnail",)

    def create(self, validated_data):
        image = Image.objects.create(**validated_data)
        return image
