from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    user_name  = models.CharField(max_length=100, unique=True)
    email_id   = models.CharField(max_length=100, unique=True)
    password   = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
