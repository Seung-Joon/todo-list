from rest_framework import generics
from rest_framework import generics
from user.models import User
from user.serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UserList(APIView):
    def get(self, request):
        try:
            user_list = User.objects.all()
            serializer = UserSerializer(user_list, many=True)
            return Response(serializer.data, status = status.HTTP_200_OK)

        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk = pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("err", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.is_valid(), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk = pk)
            user.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)