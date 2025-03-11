from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, CustomPasswordResetForm, CustomSetPasswordForm
from .models import User

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            department = form.cleaned_data.get('department')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            address = form.cleaned_data.get('address')
            group = form.cleaned_data.get('group')
            user.groups.add(group)
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'accounts/password_reset.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    template_name = 'accounts/password_reset_confirm.html'

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
@permission_required('auth.view_user', raise_exception=True)
def view_users(request):
    users = User.objects.all()
    return render(request, 'accounts/view_users.html', {'users': users})

@login_required
@permission_required('auth.change_user', raise_exception=True)
def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_users')
    else:
        form = RegisterForm(instance=user)
    return render(request, 'accounts/edit_user.html', {'form': form})

@login_required
@permission_required('auth.add_user', raise_exception=True)
def add_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_users')
    else:
        form = RegisterForm()
    return render(request, 'accounts/add_user.html', {'form': form})

@login_required
def dashboard(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})