# Generated by Django 5.0.1 on 2024-02-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bottle_size',
            field=models.IntegerField(choices=[(5, 'Large (5 Gallon)'), (3, 'Small (3 Gallon)')], verbose_name='Bottle Size'),
        ),
    ]