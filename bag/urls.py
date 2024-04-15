from django.urls import path
from . import views
urlpatterns = [
    path('',views.ViewBagTemplateView.as_view(),name='view_bag'),


]