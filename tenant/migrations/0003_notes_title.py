# Generated by Django 3.0.7 on 2020-06-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0002_auto_20200228_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
