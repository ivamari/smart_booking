from dateutil.relativedelta import relativedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from common.validators import validate_dob

User = get_user_model()


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'dob',
            'email',
            'phone',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'dob',
            'email',
            'phone',
            'password',
        )

    def validate(self, attrs):
        attrs['username'] = attrs['email']
        return super().validate(attrs)

    def validate_dob(self, value):
        return validate_dob(value)

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(password=password, **validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'dob',
            'email',
            'phone',
        )

    def validate(self, attrs):
        attrs['username'] = attrs['email']
        return super().validate(attrs)

    def validate_dob(self, value):
        return validate_dob(value)


class MeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'dob',
            'email',
            'phone',
        )
