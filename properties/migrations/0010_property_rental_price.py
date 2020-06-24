# Generated by Django 3.0.7 on 2020-06-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_auto_20200505_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='rental_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]