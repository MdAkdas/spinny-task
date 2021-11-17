from rest_framework import serializers
from .models import Box
from django.contrib.auth.models import User


class BoxSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Box
        fields = '__all__'

    def update(self, instance, validated_data):
        validated_data.pop('user', None)  # user myfield from being updated
        validated_data.pop('created_at', None)  # prevent created_at from being updated
        return super().update(instance, validated_data)