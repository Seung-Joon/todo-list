from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.Serializer):
    user_id = serializers.ReadOnlyField()
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 50)
    created_date = serializers.DateTimeField


    def create(self, validated_data):
        return User.objects.create(**validated_data)

    
    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.created_date = validated_data('created_data', instance.created_data)
        instance.save()

        return instance


