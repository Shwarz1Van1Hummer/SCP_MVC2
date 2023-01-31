from django.contrib import admin
from apps.users.models import CustomUser, Profile


@admin.register(CustomUser)
class MeinUser(admin.ModelAdmin):
    pass


admin.site.register(Profile)
