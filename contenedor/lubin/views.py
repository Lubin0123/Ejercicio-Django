from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexView(request):
      '''esta es la pagina principal'''
      return render(request, "index.html")