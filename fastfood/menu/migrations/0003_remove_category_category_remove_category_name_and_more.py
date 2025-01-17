# Generated by Django 4.2.11 on 2024-05-21 10:36

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_foodlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='category',
            name='category_slug',
            field=autoslug.fields.AutoSlugField(default='default_value', editable=False, populate_from='category_name', unique=True),
        ),
    ]
