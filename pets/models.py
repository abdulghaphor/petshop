from django.db import models

# Create your models here.
class Pet(models.Model):
	name = models.CharField(max_length=120)
	age = models.IntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=3)
	photo = models.ImageField(upload_to='pet_photos', null=True, blank=True)
	available = models.BooleanField(default=True)
	def __str__(self):
		return self.name