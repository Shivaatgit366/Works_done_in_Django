from django.shortcuts import render
from django.http import HttpResponse
from appTwo.forms import UserForm
# Create your views here.

# Import the models into the views. Then do the queries.
from appTwo.models import User

def index(request):
    return HttpResponse("<h1><em>My Second Project</em></h1>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'apptwo/help.html',context=helpdict)

def users(request):
    user_records = User.objects.order_by("id")
    userdict = {"user_table": user_records}
    return render(request,"apptwo/users2.html",context=userdict)

def forms(request):
    # creating an object.
    if request.method == "POST":
        form_object = UserForm(request.POST)

        if form_object.is_valid():
            form_object.save()  # form_object.save(commit=True) is also correct.
            print(form_object.cleaned_data["email"])
            return HttpResponse("<h1>successful</h1>")  # return users(request)  we can even call the function in the return.

        else:
            raise forms.ValidationError("not valid")

    else:  # if the request is "get request", then just take the input from the user.
        empty_form_object = UserForm()
        return render(request,"appTwo/users3.html",{"form_insert": empty_form_object})
