from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username