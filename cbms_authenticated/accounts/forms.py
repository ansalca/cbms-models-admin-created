from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import User, Student

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

class StudentUserForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'input'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    contact_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'input'}))
    date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(2000, 2025), attrs={'class': 'input'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'input'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'input'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'input'}))

    class Meta:
        model = Student
        fields = ['department', 'boarding_point', 'year', 'bus_fare_amount', 'payment_status', 'parent']
        widgets = {
            'department': forms.TextInput(attrs={'class': 'input'}),
            'boarding_point': forms.TextInput(attrs={'class': 'input'}),
            'year': forms.NumberInput(attrs={'class': 'input'}),
            'bus_fare_amount': forms.NumberInput(attrs={'class': 'input'}),
            'payment_status': forms.CheckboxInput(attrs={'class': 'input'}),
            'parent': forms.Select(attrs={'class': 'input'}),
        }