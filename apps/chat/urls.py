from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create_chat, name='home'),
    path('<str:room_name>/<str:username>/', message_view, name='room'),
]
