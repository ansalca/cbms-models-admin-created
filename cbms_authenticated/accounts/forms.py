from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User, Group

from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    department = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)))
    address = forms.CharField(widget=forms.Textarea)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, help_text="Select a group for the user")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'department', 'date_of_birth', 'address', 'group']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['department', 'date_of_birth', 'address']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input'}))


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
