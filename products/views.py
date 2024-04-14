from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView,ListView,DetailView
from .models import Product,Category


# Create your views here.



class ProductListView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = 'products_list'

    def get_queryset(self):  # sourcery skip: use-named-expression
        queryset = self.model.objects.all()

        # Filter by category
        categories = self.request.GET.get('category')
        if categories:
            categories = categories.split(',')
            queryset = queryset.filter(category__name__in=categories)

        # Filter by search query
        query = self.request.GET.get('q')
        if query:
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            queryset = queryset.filter(queries)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add search term and current categories to context
        context['search_term'] = self.request.GET.get('q')
        context['current_categories'] = Category.objects.filter(name__in=self.request.GET.get('category', '').split(','))
        
        return context
   

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_details.html"
