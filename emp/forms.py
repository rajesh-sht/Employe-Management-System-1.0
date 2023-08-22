from django import forms
from . models import Employee
from django.forms import NumberInput, TextInput, EmailInput

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        widgets = {
            'first_name': TextInput(
                attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Enter your first name'
            }),
            'last_name': TextInput(
                attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Enter your last name'
            }),
            'salary': NumberInput(
                attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Enter your salary'
            }),
            'age': NumberInput(
                attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Enter your age'
            }),
            'email': EmailInput(
                attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Enter your email address'
            }),
        }

