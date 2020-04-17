from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from user import models
import json
import datetime
from rest_framework.renderers import JSONRenderer
from user.serializer import UserSerializer
from rest_framework.parsers import JSONParser
from user.models import User

@csrf_exempt
def test(request):
    if request.method == 'GET':
        todo = models.User.objects.all()

        serializer = UserSerializer(todo, many=True)


    return JsonResponse({"Result": serializer.data})

@csrf_exempt
def registeration(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        models.User(email=body['email'],
                    password = body['pass'], 
                    created_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')).save()

    
        

