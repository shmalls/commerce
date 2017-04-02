from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import re



class SearchForm(forms.Form):
	search = forms.CharField(label='Search')

class LoginForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True)),max_length=30, label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, render_value=False)),max_length=30, label=_("Password"))

class RegistrationForm(forms.Form):
    alphaOnly = RegexValidator(r'^[a-zA-z]*$', 'Alphabet characters only allowed.')

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True)),max_length=30, label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    first_name = forms.CharField(label='First Name', validators = [alphaOnly], min_length = 2, max_length = 30)
    last_name = forms.CharField(label='Last Name', validators = [alphaOnly], min_length = 2, max_length = 30)
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True)),max_length=30, label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, render_value=False)),max_length=30, label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, render_value=False)), max_length=30, label=_("Password (again)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))


    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(_("The email already exists. Please try another one."))
        return email

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

