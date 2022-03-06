from django.urls import path
from basic_app import views


# this is for template tagging.
# We inform django that this is our app, look into the urls in this app and find the match.

app_name = "basic_app"

# to access the webpage, we should go to "domain name.basic_app.child endpoints"
# include function always focuses on child endpoints.

urlpatterns = [
    path("relative/",views.relative,name="relative"),
    path("other/",views.other,name="other"),
    path("manager/",views.manager,name="manager")
]

# domain name.basic_app.relative  ----> will take us to relative endpoint view.
# domain name.basic_app.other  ----> will take us to other endpoint view.
# domain name.basic_app.empty string  ----> will take us to basic_app endpoint view.
