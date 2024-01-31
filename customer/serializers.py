from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Customer,Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class CustomerSeializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

