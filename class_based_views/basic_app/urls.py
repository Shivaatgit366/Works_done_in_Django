from django.urls import path, include
import basic_app
from basic_app.views import SchoolDetailView, SchoolListView

app_name = "basic_app"

# mention "as_view()", then specify the name of the view
urlpatterns = [
    path("",SchoolListView.as_view(),name="schoolslist"),
    path("<int:pk>",SchoolDetailView.as_view(),name="schooldetails")
]

