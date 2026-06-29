from rest_framework import serializers
from ..models import *

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone', 'address']

    def create(self, validated_data):
        password = validated_data.pop('password')

        customer_role = Role.objects.get(name='Customer')

        user = User(
            role=customer_role,
            **validated_data
            )

        user.set_password(password)
        user.save()

        return user