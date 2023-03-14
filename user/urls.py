from django.contrib import admin
from django.urls import path,include
from .views import ManagerRegisterView,DeveloperRegisterView,UserLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
 
 path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
 path('developerregister/',DeveloperRegisterView.as_view(),name='developerregister'),
 path('login/',UserLoginView.as_view(),name='login'),
 path('logout/',LogoutView.as_view(),name='logout')
]