from django.shortcuts import render
from basicapp.forms import FormName

# Create your views here.

def index(request):
    return render(request,"basicapp/index.html")


def form_name_view(request):
    form_object = FormName()

    if request.method == "POST":
        form_object = FormName(request.POST)

        if form_object.is_valid():
            print("validation successful")
            print("name: " + form_object.cleaned_data["name"])
            print("email: " + form_object.cleaned_data["email"])
            print("text: " + form_object.cleaned_data["text"])

    form_dict = {"form_insert": form_object}
    return render(request,"basicapp/form_page.html",context=form_dict)
