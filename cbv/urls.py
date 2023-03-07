from django.contrib import admin
from django.urls import path,include
from .views import *

#from blog import views

urlpatterns = [
    
    path('create/',FoodCreateView.as_view(),name='foodcreate'),
    path('list/',FoodListView.as_view(),name='foodlist'),
    path('delete/<int:pk>',FoodDeleteView.as_view(),name='fooddelete'),
    path('update/<int:pk>',FoodUpdateView.as_view(),name='foodupdate'),
    path('detail/<int:pk>',FoodDetailView.as_view(),name='fooddetail'),
]
