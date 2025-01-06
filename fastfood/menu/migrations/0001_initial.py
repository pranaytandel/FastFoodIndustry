# Generated by Django 4.2.11 on 2024-05-19 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('category', models.CharField(choices=[('veg', 'veg'), ('non-veg', 'non-veg')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fooditem_name', models.CharField(default='product name', max_length=70)),
                ('fooditem_Ingredient', models.TextField(default='Ingredient')),
                ('fooditem_price', models.PositiveIntegerField(default=0)),
                ('fooditem_picture', models.ImageField(default='', upload_to='products/')),
            ],
        ),
    ]
