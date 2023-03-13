from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerRegisterForm

# Create your views here.
class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerRegisterForm
    template_name = 'user/manager_register.html'
    success_url = "/"