# Generated by Django 5.0.6 on 2024-08-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_alter_dailymetrics_daily_inventory_goal_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ['-is_available', '-sold', '-updated']},
        ),
        migrations.AddField(
            model_name='inventory',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='inventory',
            name='sold',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
