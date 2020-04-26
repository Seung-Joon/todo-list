# Generated by Django 3.0.4 on 2020-04-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('todo_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('complete', models.IntegerField()),
            ],
            options={
                'db_table': 'Todo',
                'managed': False,
            },
        ),
    ]
