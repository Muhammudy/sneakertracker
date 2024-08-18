# Generated by Django 5.0.6 on 2024-08-10 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_inventory_inventory_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='profit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
