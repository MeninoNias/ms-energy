# Generated by Django 5.1 on 2024-08-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='cost_per_kwh',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Custo por kWh'),
        ),
    ]
