from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
 
    path('products/',views.getAllProducts,name='getproducts'),
    path('addproduct/',views.addProducts),
    #path('deleteproduct/',views.deleteProduct),
    path('deleteproduct/<int:id>',views.deleteProduct,name='deleteproduct'),
    path('updateproduct/<int:id>',views.updateProduct),
    path('addproductwithform/',views.addProductWithForm),
    path('productdetail/<int:id>,',views.getProductDetail,name='productdetail'),
    path('update/<int:id>',views.updateProductWithForm,name ="updateproduct"),
    
    
    path('addcategory/',views.addCategory,name='addcategory'),
    path('getcategories/',views.getAllCategories,name='getcategories'),
    path('deletecategory/<int:id>',views.deleteCategory,name='deletecategory'),
    path('updatecategory/<int:id>',views.updateCat,name='updatecategory'),
    
    
    
    
]