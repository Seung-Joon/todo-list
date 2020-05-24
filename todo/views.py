from todo.models import Todo
from todo.serializer import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id', 'todo_id', 'title', 'complete']


