from django import forms
from django.forms.formsets import BaseFormSet

class CartForm(forms.Form):
	itemId = forms.IntegerField(required=False)
	name = forms.CharField(required=False, max_length=100)
	quantity = forms.IntegerField()
	total_price = forms.IntegerField(required=False)

	#def __init__:
	#	self.fields['itemId'].widget.attrs['readonly'] = True
	#	list_item = kwargs.pop('item_iterator').next()
	#	self.fields['itemId'].initial = list_item.object_id
	#	self.fields['quantity'].initial = list_item.quantity

class BaseCartFormSet(BaseFormSet):
	def clean(self):
		if any(self.errors):
			return

		ids = []
		quantity = []

		for form in self.forms:
			if form.cleaned_data:
				quantity = form.cleaned_data['quantity']