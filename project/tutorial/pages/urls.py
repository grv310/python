from django.urls import path
from .views import homePageView,debug

urlpatterns = [
    path("", homePageView, name="home"),
    path("debug", debug, name="debug"),
]
