from django.db import models
from scp.settings import MEDIA_ROOT


class SCP(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=2000)
    image = models.ImageField(verbose_name="Изображение", upload_to=MEDIA_ROOT)

    def __str__(self) -> str:
        return f"{self.id} {self.title_object}"

    class Meta:
        ordering = (
            'title_object',
        )


class SCPEuclid(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=2000)
    image = models.ImageField(verbose_name="Изображение", upload_to=MEDIA_ROOT)

    def __str__(self) -> str:
        return f"{self.id} {self.title_object}"

    class Meta:
        ordering = (
            'title_object',

        )


class SCPKetter(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=2000)
    image = models.ImageField(verbose_name="Изображение", upload_to=MEDIA_ROOT)

    def __str__(self) -> str:
        return f"{self.id} {self.title_object}"

    class Meta:
        ordering = (
            'title_object',

        )


class SCPThaumiel(models.Model):
    title_object = models.CharField(verbose_name='Название объекта фонда', max_length=255)
    description = models.CharField(verbose_name='Описание', max_length=2000)
    image = models.ImageField(verbose_name="Изображение", upload_to=MEDIA_ROOT)

    def __str__(self) -> str:
        return f"{self.id} {self.title_object}"

    class Meta:
        ordering = (
            'title_object',

        )

