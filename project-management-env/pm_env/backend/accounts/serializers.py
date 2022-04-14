from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.utils import timezone


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'user_type', 'is_active')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, password):
        if password != self.initial_data.get('confirm_password'):
            raise serializers.ValidationError("Passwords doesn't match")
        validate_password(password, self.instance)
        return password
        
    def email_to_lower(self, email):
        return email.strip().lower()

    def create(self, data):
        email = self.email_to_lower(data.get('email'))
        user = User.objects.create_user(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=email, 
            password=data.get('password'),
            user_type=data.get('user_type')
        )

        return user


# User Login Serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)

    def validate(self, data):
        email = self.email_to_lower(data.get('email'))
        password = data.get('password')
        user = authenticate(username=email, password=password)

        if user:
            if user.is_active:
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])
                return user

        message = {'email': 'The email or password is incorrect'}
        raise serializers.ValidationError(message)

    def email_to_lower(self, email):
        return email.strip().lower()