from django.db import models
from item.models import Item

#class Profile(models.Model):
#	user = models.OneToOneField(User,on_delete=models.CASCADE)
#	address = models.CharField(max_length=100, blank=True)
#	city = models.CharField(max_length=100, blank=True)
#	state = models.CharField(max_length=100, blank=True)
#	zip_code = models.CharField(max_length=100, blank=True)
#	card_number = models.IntegerField(blank=True)
#	card_name = models.CharField(max_length=100, blank=True)
#	card_month = models.IntegerField(blank=True)
#	card_year = models.IntegerField(blank=True)
#
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#        print('created profile')
#
#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
#    print('saved profile')

# Create your models here.
#class Cart(models.Model):
#	user = models.ForeignKey(User)
#	active = models.BooleanField(default=True)
#	order_date = models.DateField(null=True)
#	payment_type = models.CharField(max_length=100, null=True)
#	payment_id = models.CharField(max_length=100, null=True)
#
#	def add_to_cart(self, item_id):
#		item = Item.objects.get(pk=item_id)
#		try:
#			preexisting_order = Order.objects.get(item=item, cart=self)
#			preexisting_order.quantity+=1
#			preexisting_order.save()
#		except Order.DoesNotExist:
#			new_order = Order.objects.create(
#				item=item,
#				cart=self,
#				quantity=1
#			)
#			new_order.save()
#
#	def remove_from_cart(self, item_id):
#		item = Item.objects.get(pk=item_id)
#		try:
#			preexisting_order = Order.objects.get(item=item, cart=self)
#			if preexisting_order.quantity > 1:
#				preexisting_order.quantity -= 1
#				preexisting_order.save()
#			else:
#				preexisting_order.delete()
#		except Order.DoesNotExist:
#			pass
#			
#class Order(models.Model):
#	item = models.ForeignKey(Item)
#	cart = models.ForeignKey(Cart)
#	quantity = models.IntegerField()
