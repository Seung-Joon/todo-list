from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    user_id = serializers.ReadOnlyField()
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 50)
    created_date = serializers.DateTimeField