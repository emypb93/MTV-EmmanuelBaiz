from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.
def familiar(request):
    familiar1 = Familiar(nombre="Omar", edad=66, anio_nacimiento="1956-09-16")
    familiar1.save()
    familiar2 = Familiar(nombre="Teresa", edad=57, anio_nacimiento="1965-06-09")
    familiar2.save()
    familiar3 = Familiar(nombre="Sofia", edad=22, anio_nacimiento="2000-12-04")
    familiar3.save()
    return render(request, "index.html", {"familiar1": familiar1, "familiar2": familiar2, "familiar3": familiar3})