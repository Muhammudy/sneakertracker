# Generated by Django 5.0.6 on 2024-08-14 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_alter_inventory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ['status', '-created']},
        ),
        migrations.AddField(
            model_name='profile',
            name='company_logo',
            field=models.ImageField(default='company_pic/logo.jpg', editable=False, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic/default.jpg', null=True, upload_to='profile_pic/'),
        ),
    ]
