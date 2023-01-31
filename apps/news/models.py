from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.scp_base.models import *


class News(models.Model):
    heading = models.CharField(max_length=100)
    description_new = models.CharField(max_length=5000)
    image = models.ImageField(verbose_name="Изображение", upload_to='media/news_img/')

    def __str__(self):
        return f'{self.heading}'

    class Meta:
        ordering = (
            '-id',
        )


def scp_post_save(sender, instance, created, *args, **kwargs):
    if created:
        create_news_scp = News.objects.create(
            heading=f'Добавление объекта в фонд SCP!!! {instance.title_object}. ',
            description_new=f'Подробную информацию можете посмотреть на странице объектов класса',
            image=f'{instance.image}'
        )
        create_news_scp.save()


post_save.connect(scp_post_save, sender=SCP)
post_save.connect(scp_post_save, sender=SCPEuclid)
post_save.connect(scp_post_save, sender=SCPKetter)
post_save.connect(scp_post_save, sender=SCPThaumiel)
