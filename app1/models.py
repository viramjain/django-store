from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=150)
    product_price=models.FloatField()
    product_description=models.TextField()
    product_image = models.ImageField(upload_to="images",max_length=850)
    def __str__(self):
        return self.product_name
class Orders(models.Model):
    first_name=models.CharField(max_length=400)
    last_name=models.CharField(max_length=400)
    address=models.CharField(max_length=600)
    city=models.CharField(max_length=400)
    payment_method=models.CharField(max_length=400)
    payment_date=models.CharField(max_length=400)
    items=models.TextField()
    fulfilled=models.BooleanField(default=False)
