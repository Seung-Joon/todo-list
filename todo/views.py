from todo.models import Todo
from todo.serializer import TodoSerializer
from rest_framework import generics
from django.urls import include, path

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

urlpatterns = [
    path('', TodoList.as_view()),
    path('<int:pk>', TodoDetail.as_view())
]