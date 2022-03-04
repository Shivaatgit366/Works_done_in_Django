from django.db import models

# Create your models here. Remember to make migrations.

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)

    def __str__(self):
        return self.email
