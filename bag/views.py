from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ViewBagTemplateView(TemplateView):
    """ a View to return the index page """
    template_name = 'bag/bag.html'
