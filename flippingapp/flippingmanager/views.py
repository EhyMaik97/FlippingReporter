from django.shortcuts import render

from .models import Channel, Category, Sale, Purchase

def home(request):
    return render(request, "home.html")

def channel(request):
    channels = Channel.objects.all()
    return render(request, 'channel.html', {'channels': channels})

def category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def purchase(request):
    purchases = Purchase.objects.all()
    return render(request, 'purchase.html', {'purchases': purchases})

def sale(request):
    sales = Sale.objects.all()
    return render(request, 'sale.html', {'sales': sales})