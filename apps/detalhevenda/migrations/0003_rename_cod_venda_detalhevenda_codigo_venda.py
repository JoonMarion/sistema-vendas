# Generated by Django 4.1 on 2022-08-27 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detalhevenda', '0002_rename_qtd_produto_detalhevenda_quantidade_produto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalhevenda',
            old_name='cod_venda',
            new_name='codigo_venda',
        ),
    ]