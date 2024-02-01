from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer

from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound

# Class based view to Get User Details using Token Authentication
class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class UserSignup(APIView):
  serializer_class = RegisterSerializer

  def post(self,request,format = None):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
      saved_user = serializer.save()
      token = Token.objects.create(user = saved_user)
      return Response({'Token':token.key , 'username':saved_user.username})
    else:
      return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    