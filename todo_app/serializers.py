from rest_framework import serializers
from .models import CustomUser,Todo

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model=CustomUser
        fields=['id','username','email','role','password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'user'),  
        )
        return user

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(),required=False) 
    class Meta:
        model = Todo
        fields = ['title', 'description', 'created_at', 'expires_at','owner'] # id,owner,'updated_at' are excluded
        read_only_fields = ['created_at', 'updated_at','id']