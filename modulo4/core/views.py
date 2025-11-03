from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>")

def site(request):
    return HttpResponse("<h1> O VITOR é legal!<h1>")