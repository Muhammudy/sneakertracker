# Generated by Django 5.0.6 on 2024-08-09 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_profile_inventory_goal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
