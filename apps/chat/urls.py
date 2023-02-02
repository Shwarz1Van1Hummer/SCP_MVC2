from django.urls import path
from .views import *

urlpatterns = [
    path('message/', view_messages, name='message'),

]
