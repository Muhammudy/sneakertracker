# Generated by Django 5.0.6 on 2024-08-11 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_remove_inventory_sold_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='sold_quantity',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
