# Generated by Django 4.1 on 2022-08-28 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_alter_venda_cod_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='cod_venda',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
