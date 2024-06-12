from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sale/", views.sale, name="sale"),
    path("purchase/", views.purchase, name="purchase"),
    path("category/", views.category, name="category"),
    path("channel/", views.channel, name="channel"),
    path('statistic/', views.statistic, name='statistic'),
]