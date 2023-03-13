from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

class ManagerRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_manager = True
        user.save()
        return user    
    