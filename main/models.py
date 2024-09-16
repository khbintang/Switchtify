from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=100)
    sound_profile = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)  

    def __str__(self):
        return self.name
