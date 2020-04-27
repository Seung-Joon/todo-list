from todo.models import Todo
from todo.serializer import TodoSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import include, path

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserTodoList(APIView):
    def get(self, request, user_id):
        try:
            queryset = Todo.objects.filter(user_id=user_id)
            serializer = TodoSerializer(queryset, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)

urlpatterns = [
    path('', TodoList.as_view()),
    path('<int:pk>', TodoDetail.as_view()),
    path('user/<int:user_id>', UserTodoList.as_view())
]