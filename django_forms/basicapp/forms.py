from django import forms
# similar to models

from django.core import validators
# django.core is the module we use to check the form validation.
from django.core.exceptions import ValidationError


# ------------------------*----------------------*--------------------------*----------------------*------------

"""
# we can even write our own custom made validators.
def check_for_z(value):  # validator should check whether the "name" starts from the letter "z" or not.
    if value[0].lower() != "z":
        raise ValidationError("name does not start with 'z'")


# we have to make use of the class django.forms.Form
class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])  # we should use the parameter "validators".
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
"""


"""
    # to check the field directly without making the object, use the built in "clean_fieldname" method.
    def clean_botcatcher(self):
        bot_value = self.cleaned_data["botcatcher"]  # we get the value of botcatcher
        if len(bot_value) > 0:
            print(bot_value)
            raise forms.ValidationError("bot is present")  # print will not work after the raise/return.
        else:  # if the form is valid, then the view function will be executed.
            print("bot is not present")
"""

# -----------------------*--------------------------*-----------------------------*--------------------------


# If we want to check all the fields in one go, then we can use "clean" function.
class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")  # if we don't give label, django itself will put the label.
    text = forms.CharField(widget=forms.Textarea)

    # since we have entered the email two times, we need to check them. We can use "clean()" method.
    def clean(self):
        all_cleaned_data = super().clean()
        # make an object like this which helps to validate/check all the fields at once.
        e_mail = all_cleaned_data.get("email")  # we made an object, which is a dictionary. Keys are used to get the values.
        v_mail = all_cleaned_data["verify_email"]  # we can use ".get()" method to get the value of a key.

        if e_mail != v_mail:
            raise ValidationError("email not matched")
