from django.forms import ModelForm
from appTwo.models import User
from django.forms import Form


# creating the model form class.
class UserForm(ModelForm):
    class Meta:  # an inline class/class within the class "meta" will connect the form with the model.
        model = User
        fields = ["first_name", "last_name", "email"]  # we can even write as      fields = "__all__"
