from django.urls import path
from .views import *

urlpatterns = [
    path('nscp/', view_scp_news, name='nscp')

]
