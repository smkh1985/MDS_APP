from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers


class ProductList(APIView):
    """
    List All Products or Create a new Product
    """
    serializer_class = ProductSerializer
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            try :
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                raise serializers.ValidationError({'WaterType': 'Water and Type combination should be Unique'})

           
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

