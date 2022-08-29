# Generated by Django 4.1 on 2022-08-28 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('detalhevenda', '0005_remove_detalhevenda_cod_produto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalhevenda',
            name='cod_produto',
        ),
        migrations.AddField(
            model_name='detalhevenda',
            name='cod_produto',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='produtos.produto'),
        ),
    ]
