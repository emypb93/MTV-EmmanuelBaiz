from django.urls import path
from .views import *

urlpatterns = [
    path("familiar/", familiar, name="familiar")
]