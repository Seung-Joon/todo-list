# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from todo_list.models import ToDoList, ToDo, ToDoInfo
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

#add_todo
#delete_todo
#edit_todo
#complete_todo
#end_todo
#get_todo
#get_all_todo


info1 = ToDoInfo("todo_item_1", "new 1")
todo1 = ToDo(info1, False)
todo1.id = "1"

info2 = ToDoInfo("todo_item_2", "new 2")
todo2 = ToDo(info2, False)
todo2.id = "2"

todo_list = ToDoList([todo1,todo2])
todo_list.id = "123"

@csrf_exempt
def get_all_todo(request, id):
    if request.method == 'GET':
        todo_object = {}
        for todo in todo_list.get_all_todo().values():
            todo_object[todo.id] = {
                "title": todo.info.title,
                "description": todo.info.description,
                "flag": todo.is_complete,
            }

        return JsonResponse(todo_object)

@csrf_exempt
def get_todo(request, id, todo_id):
    if request.method == 'GET':
        todo = todo_list.get_todo(todo_id)
        todo_object = {
            "title": todo.info.title,
            "description": todo.info.description,
            "flag": todo.is_complete,
        }

        return JsonResponse(todo_object)