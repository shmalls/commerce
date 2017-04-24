from django.db import models

 Create your models here.
class Profile(models.Model):
	user = models.ForeignKey(User)
	active = models.BooleanField(default=True)
	order_date = models.DateField(null=True)
