from django.conf import settings
from django.contrib.auth import views as auth_views 
from django.urls import path, include
from users.views import (
    IndexView, 
    SignupView,
    LoginView,
    LogoutView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/registration/password_reset_complete.html'), name='password_reset_complete'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/',LoginView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
