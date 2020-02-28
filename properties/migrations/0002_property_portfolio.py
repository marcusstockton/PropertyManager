# Generated by Django 3.0.3 on 2020-02-27 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0002_remove_portfolio_property'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='portfolio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='portfolios.Portfolio'),
            preserve_default=False,
        ),
    ]
