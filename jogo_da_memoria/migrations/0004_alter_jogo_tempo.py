# Generated by Django 5.1.1 on 2024-12-15 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogo_da_memoria', '0003_alter_jogo_quantidade_alter_jogo_tempo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='tempo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
