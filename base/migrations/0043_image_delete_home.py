# Generated by Django 5.1 on 2024-08-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0042_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_goals_title', models.CharField(default='Goals', max_length=100)),
                ('image_goals', models.ImageField(default='images/goals.png', upload_to='images/')),
                ('image_inventorys_title', models.CharField(default='Inventory', max_length=100)),
                ('image_inventorys', models.ImageField(default='images/inventory.png', upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]
