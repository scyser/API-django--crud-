from rest_framework import serializers
from .models import User, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'name',
            'age',
            'about',
            'created_at',
            'is_deleted'
        ]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'priority',
            'expiration_date',
            'created_at',
            'is_deleted'
        ]

