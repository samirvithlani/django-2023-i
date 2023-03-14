from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerRegisterForm,DeveloperRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

# Create your views here.
class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerRegisterForm
    template_name = 'user/manager_register.html'
    success_url = "/"
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
        

class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperRegistrationForm
    template_name = 'user/developer_register.html'
    success_url = "/"    
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'developer'
        return super().get_context_data(**kwargs)
    


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    #success_url = "/"
    
    def get_redirect_url(self):
        if self.request.user.is_manager1:
            return '/manager/'
        else:
            return '/developer/'
        
        
    