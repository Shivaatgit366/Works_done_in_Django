from django.shortcuts import render
from django.http import HttpResponse
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
