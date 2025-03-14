from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, CustomPasswordResetForm, CustomSetPasswordForm, StudentUserForm
from .models import User, Staff, Student, Driver, Parent

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
def dashboard(request):
    user = request.user
    staff_or_student_roles = ["Staff", "Student", "Parent"]

    if user.role == 'Staff':
        user.get_profile = get_object_or_404(Staff, user=user)
        bus = user.get_profile.bus
        students = Student.objects.filter(bus=bus)
        staff_members = Staff.objects.filter(bus=bus)
        driver = bus.driver if bus else None
    elif user.role in ['Student', 'Parent']:
        if user.role == 'Student':
            user.get_profile = get_object_or_404(Student, user=user)
            bus = user.get_profile.bus
        elif user.role == 'Parent':
            user.get_profile = get_object_or_404(Parent, user=user)
            # Assuming a parent can have only one student
            student = user.get_profile.students.first()
            bus = student.bus if student else None
        students = Student.objects.filter(bus=bus) if bus else None
        staff_members = Staff.objects.filter(bus=bus) if bus else None
        driver = bus.driver if bus else None
    else:
        user.get_profile = None
        bus = None
        students = None
        staff_members = None
        driver = None

    return render(
        request,
        'dashboard.html',
        {
            'user': user,
            'bus': bus,
            'staff_or_student_roles': staff_or_student_roles,
            'students': students,
            'staff_members': staff_members,
            'driver': driver
        }
    )