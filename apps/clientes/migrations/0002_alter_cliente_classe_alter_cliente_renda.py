# Generated by Django 4.1 on 2022-08-28 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='classe',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='renda',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
