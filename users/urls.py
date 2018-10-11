from django.urls import path, include
from users.views import (
    IndexView, 
    SignupView,
)

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('signup/', SignupView.as_view(), name='signup'),
]