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

    def get_queryset(self):  

        queryset = self.model.objects.all()

        if categories := self.request.GET.get('category'):
            categories = categories.split(',')
            queryset = queryset.filter(category__name__in=categories)

        # Filter by search query
        query = self.request.GET.get('q')
        if query:
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            queryset = queryset.filter(queries)


        if sort_by := self.request.GET.get('sort'):
            direction = self.request.GET.get('dirction', 'asc')

        # Apply default sorting if no specific sorting is requested
            sort_by_default = '-created_at'  # Sort by creation date in descending order

            if sort_by == 'price':
                sort_by_field = 'price'
            elif sort_by == 'rating':
                sort_by_field = '-rating'
            elif sort_by == 'category':
                sort_by_field = 'category__name'
            else:
                sort_by_field = sort_by_default

            queryset = queryset.order_by(f'{"-" if direction == "desc" else ""}{sort_by_field}')

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
