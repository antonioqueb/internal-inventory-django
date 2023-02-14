from django.urls import path, include
from .views import RegisterView, RetrieveUserView
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('me', RetrieveUserView.as_view()),

]
