import plotly.express as px
import pandas as pd
from django.shortcuts import render
from django.db.models import Sum, Count
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

def statistic(request):
    total_purchases = Purchase.objects.aggregate(total=Sum('price'))['total']
    total_sales = Sale.objects.aggregate(total=Sum('price'))['total']
    sales = Sale.objects.all()
    total_profit = sum([sale.profit for sale in sales if sale.profit])

    purchase_channels = Purchase.objects.values('channel__name').annotate(count=Count('id')).order_by('-count')
    purchase_categories = Purchase.objects.values('category__name').annotate(count=Count('id')).order_by('-count')
    
    sale_channels = Sale.objects.values('channel__name').annotate(count=Count('id')).order_by('-count')

    purchase_channels_df = pd.DataFrame(list(purchase_channels))
    purchase_categories_df = pd.DataFrame(list(purchase_categories))
    sale_channels_df = pd.DataFrame(list(sale_channels))

    purchase_channels_fig = px.pie(purchase_channels_df, names='channel__name', values='count', title='Purchase Channels')
    sale_channels_fig = px.pie(sale_channels_df, names='channel__name', values='count', title='Sale Channels')
    purchase_categories_fig = px.pie(purchase_categories_df, names='category__name', values='count', title='Purchase Categories')

    purchase_channels_div = purchase_channels_fig.to_html(full_html=False)
    sale_channels_div = sale_channels_fig.to_html(full_html=False)
    purchase_categories_div = purchase_categories_fig.to_html(full_html=False)

    context = {
        'total_purchases': total_purchases,
        'total_sales': total_sales,
        'total_profit': total_profit,
        'purchase_channels_div': purchase_channels_div,
        'sale_channels_div': sale_channels_div,
        'purchase_categories_div': purchase_categories_div,
    }

    return render(request, 'statistic.html', context)
