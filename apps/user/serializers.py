from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64, write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8, max_length=26)
    confirm = serializers.CharField(write_only=True, min_length=8, max_length=26)

    def validate(self, data):
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        if data['password'] != data['confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64, write_only=True)
    password = serializers.CharField(write_only=True, min_length=8, max_length=16)
    
    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid username or password.")
        return data
    
    
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'telegram_id', 'telegram_username', 'phone_number']
        
    
class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField(write_only=True)
    
    def validate(self, data):
        if not data['refresh']:
            raise serializers.ValidationError("Refresh token is required.")
        if not RefreshToken(data['refresh']):
            raise serializers.ValidationError("Invalid refresh token.")
        return data