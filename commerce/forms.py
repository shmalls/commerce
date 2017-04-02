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

