# Generated by Django 4.0.6 on 2023-02-03 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_alter_card_expirations_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expirations_date',
            field=models.DateField(default=datetime.datetime(2026, 2, 2, 18, 57, 20, 688997), verbose_name='Срок годности'),
        ),
    ]
