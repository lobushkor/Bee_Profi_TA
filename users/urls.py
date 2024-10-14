from django.urls import path, include
from .views import MyLoginView, MyRegisterView, UserProfileView, ManagerProfileView
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'users'
urlpatterns = [
    path('', include('main_page.urls')),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('register/', MyRegisterView.as_view(), name='register'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='password_reset.html',
        html_email_template_name='password_reset_email.html'),
         name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('manager-profile/', ManagerProfileView.as_view(), name='manager_profile'),
]

