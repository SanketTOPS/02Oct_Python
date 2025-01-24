from django.db import models

# Create your models here.


class usersignup(models.Model):
    roll = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.BigIntegerField()
