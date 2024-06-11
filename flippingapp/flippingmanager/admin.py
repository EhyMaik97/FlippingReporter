from django.contrib import admin
from .models import Sale, Purchase, Category, Channel

admin.site.register(Sale)
admin.site.register(Purchase)
admin.site.register(Category)
admin.site.register(Channel)