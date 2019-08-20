from django.db import models

# Create your models here.

class User(models.Model):
    gender=(
        ('male',"男"),
        ('female',"女")
    )
    name = models.CharField(max_length=100)
    account = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    sex = models.CharField(max_length=32,choices=gender,default="男")
    create_time =models.DateTimeField(auto_now_add=True)
