from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import hspinfo, usrinfo,  User



class HospitalReg(UserCreationForm):
  
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta(UserCreationForm):
        model = User
        fields = ['id','email','username']

    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_hospital = True
        user.save()
        hosp = hspinfo.objects.create(user=user)
        return user

class UserReg(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta(UserCreationForm):
        model  = User
        fields = ['id','email','username']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_user = True
        user.save()
        usr = usrinfo.objects.create(user=user)
        return user