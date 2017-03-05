from django.db import models
from item.models import Item

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
