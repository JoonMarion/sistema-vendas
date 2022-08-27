# Generated by Django 4.1 on 2022-08-27 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('cod_produto', models.AutoField(primary_key=True, serialize=False)),
                ('unidade', models.CharField(choices=[('UN', 'Unidade'), ('GR', 'Grama'), ('KG', 'Quilograma'), ('L', 'Litro'), ('ML', 'Mililitro'), ('PACOTE', 'Pacote'), ('MT', 'Metro')], max_length=30)),
                ('descricao', models.CharField(max_length=100)),
                ('valor_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque_minimo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade_estoque', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]