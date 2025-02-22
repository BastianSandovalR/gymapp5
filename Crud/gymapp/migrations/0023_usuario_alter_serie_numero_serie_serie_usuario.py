# Generated by Django 5.1.4 on 2025-02-02 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0022_serie_numero_serie_alter_rutina_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='serie',
            name='numero_serie',
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name='serie',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gymapp.usuario'),
        ),
    ]
