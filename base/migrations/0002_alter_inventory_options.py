# Generated by Django 5.0.6 on 2024-07-26 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
