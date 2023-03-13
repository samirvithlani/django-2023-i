from django.contrib import admin
from django.urls import path,include
from .views import ManagerRegisterView
urlpatterns = [
 
 path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
]