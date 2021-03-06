from dataclasses import fields
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

# put paranthesis for multi-line importing
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                   CreateView, DeleteView, UpdateView)
from typing import Dict, Any
from basic_app.models import School, Student


# Create your views here.

"""
def index(request):
    return render(request,"index.html")
"""


"""
class CBView(View):
    
    # we can write all the required functions here inside the class.
    def get(self,request):
        return render(request,"index.html")
"""


"""
class CBTView(TemplateView):
    # this class is the child class. It has been inherited from "TemplateView" class.
    # instead of using "render" function, we can simply give "template_name" as class/object attribute.
    # we can send context dictionary also.
    template_name = "index.html"
    temp_object = TemplateView()
    context_dict = {"inject_me": temp_object}
"""


"""
we can even update the attributes inside the "as_view" function as shown below, Or you can inherit from TemplateView class.
Both the methods give the same result.

from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('about/', TemplateView.as_view(template_name="about.html")),
]
"""


class CBTView(TemplateView):
    # This class has been inherited from "TemplateView" class.
    # we can send "context dictionary" directly as shown in the above example.
    # to get the context dictionary, we can use "get_context_data" function as shown in the below example.

    template_name = "index.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        temp_object = super().get_context_data(**kwargs)
        # temp_object is a dictionary/object made from "super" function.
        # temp_object will be printed as {'view': <basic_app.views.CBTView object at 0x0000028740EE01F0>}
        # we can add both the "keys" and "values" to that dictionary.
        
        temp_object["inject_me"] = "Hello Developers"
        print(temp_object)  # {'view': <basic_app.views.CBTView object at 0x0000028740EE01F0>, 'inject_me': 'Hello Developers'}
        return temp_object


class SchoolListView(ListView):  # inheriting from the built-in CBV "ListView".
    model = School  # mention the name of the model.
    template_name = "basic_app/school_list.html"  # mention the name of the template.

    # django automatically does this command    School.objects.all()
    # School.objects.all() --> this gives the list of all row objects present inside that table.
    context_object_name = "list_of_school_objects"  # this is the "key" in the context dictionary.

    # to get the context dictionary, we can use "get_context_data" function.
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont_dict = super().get_context_data(**kwargs)
        print(cont_dict)
        # cont_dict["list_of_school_objects"] = School.objects.all()        this line not required since we used "context_object_name"
        return cont_dict


class SchoolDetailView(DetailView):  # inheriting from the built-in CBV "DetailView"
    model = School  # mention the name of the model.
    template_name = "basic_app/school_detail.html"  # mention the name of the template.

    # "context_object_name" gives only one row object.
    context_object_name = "school_object"  # this is the "key" in the context dictionary.

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        cont_dict = super().get_context_data(**kwargs)
        print(cont_dict)
        return cont_dict


class SchoolCreateView(CreateView):
    # this "CreateView" cbv creates a model-form. We should specify the model name and fields to be displayed.
    # then it creates an object called "form" ----> it is a model-form object.
    # then it saves the object into the database row automatically.
    # in the template, keep the name of the file as "model_form.html".
    model = School
    fields = ["name", "principal", "location"]


class SchoolUpdateView(UpdateView):
    # "UpdateView" cbv updates the object present in the database. It takes the model name, fields for updating.
    # an object of "model_form" will be formed. After getting the data from the user, it saves it in the database.
    model = School
    fields = ["name", "principal"]
    template_name_suffix = "_update_form"


class SchoolDeleteView(DeleteView):
    # "DeleteView" cbv deletes the row object present in the database. It takes the model name.
    model = School  # a local object called "school" will be automatically created by django when we mention model name.
    success_url = reverse_lazy("basic_app:schoolslist")

    # Remember:- An object called "school" will be created by django when we give the name of the model.
    # So, we can directly use {{ school.name }} in our relevant template file.
