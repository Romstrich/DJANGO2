from django.db import models

# Create your models here.

#Модель для категорий
class Product_Category(models.Model):
    name=models.CharField(max_length=64)
    description=models.TextField(blank=True,null=True)

class Product(models.Model):
    name = models.CharField(max_length = 64)
    image = models.ImageField(upload_to='product_image',blank=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Product_Category,on_delete=models.CASCADE)


