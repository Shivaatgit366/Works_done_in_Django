from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo  # this is the table we created in the database.


# A model form is linked to one table only.
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ["portfolio_site", "profile_pic"]

# Remember:- There are two tables. Django provides a table called "auth_user" (that's the "User" model).

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput()) # not necessary since "password" field is already built-in.

    class Meta():
        model = User
        fields = ["username", "email", "password"]


# we are not creating any form for the "login", we are directly using html forms in this project.

