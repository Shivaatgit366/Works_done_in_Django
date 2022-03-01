from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Import the models into the views. Then do the queries.
from first_app.models import Topic, Webpage, AccessRecord


def welcome(request):
    return HttpResponse("<h1>Welcome to the Website</h1>")

def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": webpages_list}
    return render(request, "first_app/index.html", context=date_dict)
