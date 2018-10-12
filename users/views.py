from django.conf import settings
from django.contrib.auth import (
    login,
    logout,
)
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import (
    View, 
    TemplateView
)
from users.forms import (
    UserRegistrationForm, 
    LoginForm, 
)


class IndexView(TemplateView):
    template_name = 'users/index.html'


class SignupView(TemplateView):
    template_name = 'users/signup.html'

    def get(self, *args, **kwargs):
        form = UserRegistrationForm()
        return render(self.request, self.template_name, {'form': form})

    def post(self, *args, **kwargs):
        form = UserRegistrationForm(self.request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('index'))
        return render(self.request, self.template_name, {'form': form})


class LoginView(TemplateView):
    template_name = 'users/login.html'

    def get(self, *args, **kwargs):
        form = LoginForm()
        return render(self.request, self.template_name, {'form': form})

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            user = form.user_cache
            login(self.request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(self.request, self.template_name, {'from': form})


class LogoutView(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return HttpResponseRedirect(reverse('index'))