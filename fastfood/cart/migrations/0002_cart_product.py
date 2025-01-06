# Generated by Django 4.2.11 on 2024-05-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_foodlist_product_category_id'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(through='cart.CartItem', to='menu.foodlist'),
        ),
    ]