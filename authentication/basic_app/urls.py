from django.urls import path
from basic_app import views


# Remember:- For the sake of template URLs, give the name of the app.
app_name = "basic_app"  # namespace should be provided, see the documentation    https://docs.djangoproject.com/en/4.0/topics/http/urls/#term-application-namespace


urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.my_login_view,name="my_login")
]
