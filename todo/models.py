# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    complete = models.IntegerField()
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Todo'
