from django.urls import path

from .views import UserSignup
from rest_framework.authtoken import views
urlpatterns = [
  path('sign-up',UserSignup.as_view()),
  path('api-token-auth', views.obtain_auth_token)
]