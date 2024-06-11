from django.db import models
from django.utils import timezone


class Channel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.date.strftime("%d/%m/%Y")}"


class Sale(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, limit_choices_to={'sale__isnull': True})
    date = models.DateField(default=timezone.now)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.purchase.name} - {self.date.strftime('%d/%m/%Y')}"

