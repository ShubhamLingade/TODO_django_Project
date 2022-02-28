from django.db import models

# Create your models here.
class Task(models.Model):
    task_name=models.CharField(max_length=30)

class Task_list(models.Model):
    task_list=models.CharField(max_length=100)

class Custem(models.Model):
    custem=models.CharField(max_length=50)

class Tags(models.Model):
    tags=models.CharField(max_length=30)
