import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


import datetime



today = datetime.date.today()
MONTH_CHOICES = [(m, datetime.date(today.year, m, 1).strftime('%b')) for m in range(1, 13)]
YEAR_CHOICES = [(y, y) for y in range(today.year, today.year + 21)]


class EditProfileForm(forms.ModelForm):
    alphaOnly = RegexValidator(r'^[a-zA-z]*$', 'Alphabet characters only allowed.')

    first_name = forms.CharField(label='First Name', validators = [alphaOnly], min_length = 2, max_length = 30)
    last_name = forms.CharField(label='Last Name', validators = [alphaOnly], min_length = 2, max_length = 30) 
    email = forms.EmailField(label='Email Address')
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']
