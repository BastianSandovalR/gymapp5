# Generated by Django 5.1.4 on 2025-01-31 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0021_remove_serie_notas_remove_serie_serie_numero_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='numero_serie',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='serie',
            name='peso',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='serie',
            name='repeticiones',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='serie',
            name='rutina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to='gymapp.rutina'),
        ),
    ]
