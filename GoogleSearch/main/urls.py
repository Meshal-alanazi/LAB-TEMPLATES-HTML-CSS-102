from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("",views.home_view,name="home_view"),
    path("terms/",views.service_page,name="service_page")
]