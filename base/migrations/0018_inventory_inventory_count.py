# Generated by Django 5.0.6 on 2024-08-10 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_inventory_profit_inventory_sold_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='inventory_count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
