from user.models import User
from user.serializer import UserSerializer
from rest_framework import generics
from django.urls import include, path

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>', UserDetail.as_view())
]