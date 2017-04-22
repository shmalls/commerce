from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from item.models import Item
from purchase.choices import *

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	address = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=100, blank=True)
	state = models.CharField(max_length=100, blank=True)
	zip_code = models.CharField(max_length=100, blank=True)
	card_number = models.IntegerField(null=True)
	card_name = models.CharField(max_length=100, blank=True)
	card_month = models.IntegerField(choices=MONTH_CHOICES,default=1)
	card_year = models.IntegerField(choices=YEAR_CHOICES,default=1)

	def getCardNumber(self):
		return str(self.card_number)[-4:].rjust(len(str(self.card_number)), "*")

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['address', 'city', 'state', 'zip_code']

class PaymentForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['card_number','card_name','card_month','card_year']
		labels = {'card_month':'Expiration Month','card_year':"Expiration Year"}

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class ItemOrder(models.Model):
	itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField()
	orderId = models.ForeignKey('Order',on_delete=models.CASCADE)

	def total(self):
		return self.quantity * self.itemId.price

class Order(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	purchase_date = models.DateField(auto_now_add=True)
	address = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=100, blank=True)
	state = models.CharField(max_length=100, blank=True)
	zip_code = models.CharField(max_length=100, blank=True)
	card_number = models.IntegerField(null=True)
	card_name = models.CharField(max_length=100, blank=True)
	card_month = models.IntegerField(null=True)
	card_year = models.IntegerField(null=True)

	def getCardNumber(self):
		return str(self.card_number)[-4:].rjust(len(str(self.card_number)), "*")
