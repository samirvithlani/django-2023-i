from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function based view , class based view


def home(request):
    return HttpResponse("HOME")
    
def index(request):
    return HttpResponse("Hello World")

def aboutUs(request):
    return render(request,'aboutus.html')

def contactUs(request):
    name = "Ravi"
    email ="ravi@gmail.com"
    return render(request,'blog/contactus.html',{'name':name,'email':email})
    
def feedback(request):
    
    userName = "parth"
    userEmail = "parth@gmail.com"
    context ={
        'userName':userName,
        'userEmail':userEmail,
    }
    
    
    return render(request,'blog/feedback.html',context)
