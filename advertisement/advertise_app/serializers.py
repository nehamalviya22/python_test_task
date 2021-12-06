from rest_framework import serializers
from .models import username,sdkversion

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = username
        fields = "__all__"


class SdkversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = sdkversion
        fields = "__all__"