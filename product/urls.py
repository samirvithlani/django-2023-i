from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
 
    path('products/',views.getAllProducts),
    path('addproduct/',views.addProducts),
    #path('deleteproduct/',views.deleteProduct),
    path('deleteproduct/<int:id>',views.deleteProduct),
    path('updateproduct/<int:id>',views.updateProduct),
    path('addproductwithform/',views.addProductWithForm),
]