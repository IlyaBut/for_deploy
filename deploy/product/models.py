from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField()
    article = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products")

    def __str__(self):
        return self.name
