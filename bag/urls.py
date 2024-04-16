from django.urls import path
from . import views
urlpatterns = [
    path('',views.ViewBagTemplateView.as_view(),name='view_bag'),
    path('add/<int:item_id>/', views.AddToBagView.as_view(), name='add_to_bag'),


]