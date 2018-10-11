from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import View, TemplateView
from users.forms import UserRegistrationForm


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


