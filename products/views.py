from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import TemplateView,ListView,DetailView
from .models import Product


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = 'products_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            return self.model.objects.filter(queries)
        else:
            return self.model.objects.all()
        

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse_lazy('products'))
        return super().get(request, *args, **kwargs)

"""  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_term'] = self.request.GET.get('q')
        return context """

   

class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_details.html"
