# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ToDoInfo:
    def __init__ (self, title, description):
        self.title = title
        self.description = description


class ToDo:
    def __init__(self, info, is_complete):
        self.id = ""
        self.info = info
        self.is_complete = is_complete


class ToDoList:
    def __init__ (self, todo_list):
        self.id = ""
        self.todo_object = {}
        for todo in todo_list:
            self.todo_object[todo.id] = todo

    def add_todo(self, id, todo):
        self.todo_object[id] = todo

    def delete_todo(self, id):
        self.todo_object.pop(id)

    def edit_todo(id, info):
        self.get_todo(id).info = info

    def set_complete_todo(self, id):
        self.get_todo(id).is_complete = True

    def set_end_todo(self, id):
        self.get_todo(id).is_complete = False

    def get_todo(self, id):
        return self.todo_object[id]

    def get_all_todo(self):
        return self.todo_object
        
        

    




#add_todo
#delete_todo
#edit_todo
#complete_todo
#end_todo
#get_todo
#get_all_todo

