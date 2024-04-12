from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexTemplateView(TemplateView):
    """ a View to return the index page """
    template_name = 'home/index.html'
