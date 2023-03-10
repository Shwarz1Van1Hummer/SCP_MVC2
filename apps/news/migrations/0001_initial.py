# Generated by Django 4.0.6 on 2022-09-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='media/news_img/', verbose_name='Изображение')),
            ],
        ),
    ]
