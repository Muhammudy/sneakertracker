# Generated by Django 5.0.6 on 2024-08-14 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_alter_profile_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company_logo',
            field=models.ImageField(default='company/logo.png', upload_to=''),
        ),
    ]
