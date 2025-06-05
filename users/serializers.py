from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields ="__all__"

    def create(self,data):
        user=User.objects.create(**data)
        return user
    
class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields ="__all__"