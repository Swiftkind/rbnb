from django import forms
from users.models import User
from django.contrib.auth import authenticate


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(attrs={'minLength': 8}), required=True)

    class Meta:
        model = User
        fields = ( 'email', 'first_name', 'last_name', 'password',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already taken.')

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)
        if commit:
            instance.set_password(self.data['password'])
            instance.save()
        return instance


class LoginForm(forms.Form):    
    user_cache = None

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        email = email.lower()
        password = self.cleaned_data.get('password')
        
        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError('Invalid Email or Password.')
        else:
            self.user_cache=user

        return self.cleaned_data
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         