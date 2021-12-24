from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import NoramlText
class NormalTextView(generic.ListView):
    model = NoramlText
    template_name = 'mainfile.html'
