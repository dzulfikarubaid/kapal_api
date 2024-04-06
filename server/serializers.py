from rest_framework import serializers
from app.models import User

class UserSerializer(serializers.ModelSerializer):
    position = serializers.CharField(max_length=40, allow_blank=False)
    confirm_password = serializers.CharField(max_length=100, write_only=True)
    name = serializers.CharField(max_length=40, allow_blank=False)
    email = serializers.EmailField(max_length=60, allow_blank=False)
    class Meta:
        model = User
        fields = ['id','name', 'username', 'password', 'position','email', 'confirm_password']
    
    def validate(self, data):
        if data['password'] != data.get('confirm_password'):
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password from data
        user = User.objects.create_user(**validated_data)
        return user