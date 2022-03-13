from distutils.command.upload import upload
from django.db import models

from django.contrib.auth.models import User
# "models.User" and "models.UserManager" are the inbuilt models/classes best suitable for the authorization.
# these classes are inbuilt in django and they have specific fields, functions inside them.
# these inbuilt class functions help for the authorization.


# Create your models here.


# User model already has fields like "username", "email", "firstname", "lastname".
# this below model is created to provide additonal fields apart from User model.


"""
class OneToOneField:-
Multi-table inheritance concept is explained here.
Here, columns from the other table is inherited as the foreign keys into the present table.
It is similar to a ForeignKey with unique=True.
Instead of inheriting individual columns as foreign keys, we are inheriting all the fields from the other table directly.
We have classes like "OneToOneField", "ManyToManyField", "OneToManyField" etc.
"""


# Django provides a table called "auth_user" (that's the "User" model).
# This "auth_user" table is built-in. It is the "User" model.


# If we inherit from "model.User" class directly, it will spoil the database.
class UserProfileInfo(models.Model):  # From parent table all the columns are inherited and they are saved as individual objects in the child table.
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # columns from the "User" table are inherited and saved as objects in this table under "user" field.
    
    # additional things required.
    portfolio_site = models.URLField(blank=True)  # URL field gives web address. It is not mandatory.

    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)  # Image filed takes the images of the user.


    def __str__(self):
        return self.user.username


# we are not creating any form for the "login", we are directly using html forms in this project.
