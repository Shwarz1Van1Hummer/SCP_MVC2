# Generated by Django 4.0.6 on 2022-07-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SCP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_object', models.CharField(max_length=255, verbose_name='Название объекта фонда')),
                ('description', models.CharField(max_length=2000, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Изображение')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
