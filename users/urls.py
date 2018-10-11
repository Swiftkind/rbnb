from django.urls import path, include
from users.views import (
    IndexView, 
    SignupView,
    LoginView,
)

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login')
]
