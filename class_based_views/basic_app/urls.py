from django.urls import path, include
import basic_app
from basic_app.views import SchoolCreateView, SchoolDeleteView, SchoolDetailView, SchoolListView, SchoolUpdateView

app_name = "basic_app"

# mention "as_view()", then specify the name of the view
urlpatterns = [
    path("",SchoolListView.as_view(),name="schoolslist"),
    path("create/",SchoolCreateView.as_view(),name="createschool"),
    path("<pk>/",SchoolDetailView.as_view(),name="schooldetails"),
    path("update/<pk>/",SchoolUpdateView.as_view(),name="updateschool"),
    path("delete/<pk>/",SchoolDeleteView.as_view(),name="deleteschool")
]
