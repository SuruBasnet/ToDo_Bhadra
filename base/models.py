from django.db import models

# Create your models here.
class ToDo(models.Model):
    status_list = [('Done','Done'),('In progress','In progress'),('Not done','Not done')]

    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=50,choices=status_list)