from django.db import models
from django import forms

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=100)
	seller_name = models.CharField(max_length=100)
	price = models.FloatField()

	def __str__(self):
		return self.name

class Review(models.Model):
	itemId = models.ForeignKey('Item',on_delete=models.CASCADE)
	review = models.TextField(max_length=500)
	
	def counter(low, high):
		current = low
		while current <= high:
			yield current
			current += 1
	
class ReviewForm(forms.ModelForm):
	
	review = forms.CharField(widget=forms.Textarea, label='')
	class Meta:
		model = Review
		fields = ['itemId', 'review']
		widgets = {'itemId': forms.HiddenInput()}