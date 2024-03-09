from django.shortcuts import render,redirect
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name='base.html'

