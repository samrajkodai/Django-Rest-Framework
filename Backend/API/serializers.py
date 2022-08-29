from rest_framework import serializers
from .models import APIModel

class APISerializers(serializers.ModelSerializer):
    class Meta:
        model=APIModel
        fields=[
            'name',
            'age',
            'location'
        ]