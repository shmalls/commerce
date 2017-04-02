from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=100)
	seller_name = models.CharField(max_length=100)
	price = models.FloatField()

	def __str__(self):
		return self.name

class Review(models.Model):
	itemId = models.ForeignKey('Item',on_delete=models.CASCADE)
	review = models.CharField(max_length=500)