from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import user_login, user_logout, CustomPasswordResetView, CustomPasswordResetConfirmView, home, dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('', home, name='home'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
    # Include default auth URLs
    path('', include('django.contrib.auth.urls')),
]
