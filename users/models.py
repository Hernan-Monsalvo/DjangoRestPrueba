from django.db import models

class User(models.Model):

    class Meta:
        db_table = "Users"

    name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)