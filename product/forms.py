import django.forms as form
from .models import Product

class ProductForm(form.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'