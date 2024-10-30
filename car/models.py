from django.contrib.auth.models import User
from django.db import models
from Brand.models import BrandModel

class CarModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='car/media/car_images/')
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='cars')
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    purchased_by = models.ManyToManyField(User, related_name='purchased_cars', blank=True)  

    def __str__(self):
        return self.name
