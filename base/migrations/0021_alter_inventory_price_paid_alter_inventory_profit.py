# Generated by Django 5.0.6 on 2024-08-10 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_inventory_price_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='price_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
