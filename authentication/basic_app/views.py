from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render
import basic_app
from basic_app.forms import UserForm, UserProfileInfoForm

# -----------------------------------------------------------------------------------------------------------
# import the things required for "login".

from django.contrib.auth.decorators import login_required  # "login_required" is a decorator.
from django.contrib.auth import authenticate, login  # as per the django documentation, we should use both authenticate() and login() functions.
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout  # when login is imported, we should also import logout function.

# -----------------------------------------------------------------------------------------------------------


# Create your views here.

def index(request):
    return render(request,"basic_app/index.html")

# -----------------------------------------------------------------------------------------------------------

# for login.

@login_required
def special(request):
    return HttpResponse("<h1>You are successfully logged in</h1>")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

# ----------------------------------------------------------------------------------------------------------


def register(request):
    if request.method == "POST":
        user_form_object = UserForm(request.POST)  # we can even write as    UserForm(data=request.POST)
        profile_form_object = UserProfileInfoForm(request.POST)

        if user_form_object.is_valid() and profile_form_object.is_valid():
            user_db_obj = user_form_object.save(commit=False)
            # assignment of the save method result.
            user_db_obj.set_password(user_db_obj.password)  # Hashing the plain password in the database.
            user_db_obj.save()  # by default, save() method keeps "commit=True"
    
            # Now we deal with the extra info!

            profile_db_obj = profile_form_object.save(commit=False)

            # Set One to One relationship between
            # User_db_obj and Profile_db_obj
            profile_db_obj.user = user_db_obj

            # Check if they provided a profile picture
            if "profile_pic" in request.FILES:
                # request.FILES gives a dictionary which will have the key "profile_pic" and value will be an image file path.
                print("there is an image")
                # If yes, then grab it from the POST form reply
                profile_db_obj.profile_pic = request.FILES["profile_pic"]
            
            # Now save the model
            profile_db_obj.save()

            # we can do like    registered = False can be changed to registered = True
            # we can write like    display_dict = {"user_object": user_db_obj, "profile_object": profile_db_obj, "registered": registered}

            # for "post" request, render the view with below dictionary
            display_dict = {"user_object": user_db_obj, "profile_object": profile_db_obj, "registered": True}

        else:
            raise ValidationError("form is not valid")

    # for "get" request below code will be executed
    else:
        empty_user_object = UserForm()
        empty_profile_object = UserProfileInfoForm()

        # for "get" request, render the view with below dictionary
        display_dict = {"user_object": empty_user_object, "profile_object": empty_profile_object, "registered": False}
    

    # for any kind of requests, just render the below code
    return render(request,"basic_app/registration.html",context=display_dict)
# -------------------------------------------------------------------------------------------------------------


def my_login_view(request):

    if request.method == "POST":

        # request.POST is a dictionary.
        # we will pick the values for "username" and "password" in the request.POST dictionary.
        username = request.POST["username"]
        password = request.POST["password"]

        # we use authenticate() function to find the existing user object.
        existing_user = authenticate(request, username=username, password=password)

        if existing_user is not None:  # we can even write    "if existing_user:"
            # check for active account. Never login directly.
            if existing_user.is_active:
                login(request, existing_user)

                # reverse looks at your urls.py and looks for the name you pass it
                # The name of the app should be specified, for example    return HttpResponseRedirect(reverse('basic_app:special'))
                # Send the user back to some other page using "response redirect" and "reverse" functions. In this case their homepage.
                return HttpResponseRedirect(reverse("index"))

            else:
                # account is not active.
                return HttpResponse("<h1>account is not active</h1>")

        else:
            # raise error.
            print("Someone tried to login and failed.")
            print(f"Someone tried to login with username:{username} and password:{password}")
            return HttpResponse("<h1>Invalid Login</h1>")
    

    else:  # in get request, we just render the "login.html" page.
        return render(request,"basic_app/login.html",context={})  # context dictionary is empty because we are not returning any object/variable as template variables.

