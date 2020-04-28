from todo.models import Todo
from todo.serializer import TodoSerializer
from rest_framework import generics
from django.urls import path
from django_filters.rest_framework import DjangoFilterBackend

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['todo_id', 'user']


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


urlpatterns = [
    path('', TodoList.as_view()),
    path('<int:pk>', TodoDetail.as_view())
]

