from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

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
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}"


class Sale(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, limit_choices_to={'sale__isnull': True})
    date = models.DateField(default=timezone.now)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    fee = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')
    shipping_cost = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR') 
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='EUR')

    
    def __str__(self):
        return f"{self.purchase.name} - {self.date.strftime('%d/%m/%Y')}"

    @property
    def profit(self):
        if self.price and self.fee and self.shipping_cost and self.purchase.price:
            return self.price - self.fee - self.shipping_cost - self.purchase.price
        return f'0.00€'
