# Generated by Django 4.2.11 on 2024-05-31 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_foodlist_product_category_id'),
        ('cart', '0003_order_rename_product_cart_products_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('productref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.foodlist')),
            ],
        ),
    ]
