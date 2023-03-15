from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import Food,AddFile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class FoodCreateView(CreateView):
    fields  ='__all__'
    model = Food
    template_name = 'cbv/foodcreate.html'
    success_url = '/cbv/list'

#@login_required
#@method_decorator(login_required, name='dispatch')
@method_decorator(login_required(login_url='/user/login'), name='dispatch')

class FoodListView(ListView):
    model = Food
    template_name = 'cbv/foodlist.html'
    context_object_name = 'foodlist'

class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'cbv/fooddelete.html'
    success_url = '/cbv/list'  


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'cbv/foodupdate.html'
    fields = '__all__'
    success_url = '/cbv/list'      
    
class FoodDetailView(DetailView):
    model = Food
    template_name = 'cbv/fooddetail.html'
    context_object_name = 'fooddetail'    
    
class AddFileView(CreateView):
    model = AddFile
    template_name = 'cbv/addfile.html'
    success_url = '/cbv/filelist'
    fields = '__all__'
    
class FileListView(ListView):
    model = AddFile
    template_name = 'cbv/filelist.html'
    context_object_name = 'filelist'
    
    