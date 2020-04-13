from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from user import models
import json
import datetime

@csrf_exempt
def test(request):
    if request.method == 'GET':
        models.User(email="123@test.1com", password = "321t1est", created_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')).save()
        todo = models.User.objects.all()

    return JsonResponse({"Result": str(todo)})