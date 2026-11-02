from rest_framework import serializers
from store_project.models import Product
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        read_only_fields=["id"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["id","name","description","category","price","stock","created_at"]
        read_only_fields=["id","created_at"]
