from django.db.models.enums import Choices
from django.forms import ModelForm, fields, models
from django.contrib.auth.models import User
from adminpanel.models import EmployeeDetails
from django import forms
from django.contrib.auth.forms import UserCreationForm





class EmployeeForm(ModelForm):
    class Meta:
        model=EmployeeDetails
        fields="__all__"
        options=(
        ("fulltime","fulltime"),
        ("parttime","parttime"),

        )
        gender_option=(
        ("male","male"),
        ("female","female")
        )
        widgets={
            'dob':forms.DateInput(attrs={'class':"form-control"}),
            'name':forms.TextInput(attrs={'class':"form-control"}),
            'image':forms.FileInput(attrs={'class':"form-control"}),
            'email':forms.EmailInput(attrs={'class':"form-control"}),
            'password':forms.PasswordInput(attrs={'class':"form-control"}),
            'phone':forms.NumberInput(attrs={'class':"form-control"}),
            'address':forms.TextInput(attrs={'class':"form-control"}),
            'Employment_type':forms.Select(choices=options,attrs={'class':"form-control"}),
            'age':forms.NumberInput(attrs={'class':"form-control"}),
            'gender':forms.Select(choices=gender_option,attrs={'class':"form-control"}),
            'position':forms.TextInput(attrs={'class':"form-control"}),
            


        }
        
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]

class SignInForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
