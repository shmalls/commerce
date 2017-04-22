from django.db import models
from django import forms
from django.contrib.auth.models import User
import os


# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=100)
	seller_name = models.CharField(max_length=100)
	price = models.FloatField()
	description = models.TextField(max_length=500)
	image = models.ImageField(blank=True, null=True)


	def __str__(self):
		return self.name

class Review(models.Model):
	itemId = models.ForeignKey('Item',on_delete=models.CASCADE)
	review = models.TextField(max_length=500)
	user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)

	
	def counter(low, high):
		current = low
		while current <= high:
			yield current
			current += 1
	
class ReviewForm(forms.ModelForm):
	
	review = forms.CharField(widget=forms.Textarea, label='')
	class Meta:
		model = Review
		fields = ['itemId', 'review', 'user']
		widgets = {'itemId': forms.HiddenInput(), 'user' : forms.HiddenInput()}