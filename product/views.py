from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework import serializers


from rest_framework.exceptions import NotFound, ValidationError 
from django.http import Http404
from django.shortcuts import get_object_or_404


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
                raise ValidationError({'WaterType': 'Water and Type combination should be Unique'})

           
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    serializer_class = ProductSerializer

    def get(self,request , pk,format =None):

        product = get_object_or_404(Product,pk = pk)
        # ====> OR Begin <=====
        # try :
        #     product = Product.objects.get(id=pk)
        # except Product.DoesNotExist:
        #     raise NotFound
        # ====> OR End <=====
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        product = get_object_or_404(Product,pk = pk)
        serializer = ProductSerializer(product, data = request.data , partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)
            except:
                raise ValidationError({'WaterType': 'Water and Type combination should be Unique'})
        else:
            # raise ValidationError
            print(serializer.data)
            return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format = None):
        product = get_object_or_404(Product,pk = pk)
        product.delete()
        return Response(status= status.HTTP_204_NO_CONTENT) # the best response for deletion is HTTP204