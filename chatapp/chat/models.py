from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name  = models.CharField(max_length=20)
    user_name  = models.CharField(max_length=50)
    email_id   = models.CharField(max_length=50)
    password   = models.CharField(max_length=50)
