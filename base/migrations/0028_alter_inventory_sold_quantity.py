# Generated by Django 5.0.6 on 2024-08-11 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_inventory_sold_quantity_alter_inventory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='sold_quantity',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
