from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Product


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = 'products_list'