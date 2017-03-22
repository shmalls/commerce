from django import forms
from .choices import *

class ShippingForm(forms.Form):
	first_name = forms.CharField(label='First Name', max_length=100)
	last_name = forms.CharField(label='Last Name', max_length=100)
	address = forms.CharField(label='Address', max_length=100)
	city = forms.CharField(label='City', max_length=100)
	state = forms.CharField(label='State', max_length=100)
	#country = forms.CharField(label='Country', max_length=100)
	zip_code = forms.CharField(label='Zip', max_length=100)

class PaymentForm(forms.Form):
	card_number = forms.IntegerField(label='Card number')
	name = forms.CharField(label='Name on card', max_length=100)
	exp_date_month = forms.ChoiceField(choices=MONTH_CHOICES)
	exp_date_year = forms.ChoiceField(choices=YEAR_CHOICES)

