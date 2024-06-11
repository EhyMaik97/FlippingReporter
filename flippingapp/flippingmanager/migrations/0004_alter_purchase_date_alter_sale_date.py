# Generated by Django 5.0.6 on 2024-06-11 16:14

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flippingmanager', '0003_purchase_is_sold_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]