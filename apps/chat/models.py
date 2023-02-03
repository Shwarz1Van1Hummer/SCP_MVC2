from django.db import models
from datetime import datetime
from apps.users.models import *


class Message(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=datetime)

    def __str__(self):
        return f'{self.message}'

    class Meta:
        ordering = (
            'date',
        )
