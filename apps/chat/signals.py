from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Message
from apps.users.models import Profile


def message_post(sender, instance, created, *args, **kwargs):
    if created:
        create_message = Message.objects.create(
            user=f'{instance.user}',
            message=f'{instance.message}',
            date=f'{instance.date}'
        )
        profile_get = Profile.objects.get(
            user=f'{instance.user}',
            image=f'{instance.image}'
        )
        create_message.save()
        profile_get.save()


post_save.connect(message_post, sender=Message)
