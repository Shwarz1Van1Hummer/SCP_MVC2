from django.urls import path
from .views import *

urlpatterns = [
    path('nscp/', view_scp_news, name='nscp'),
    path('del_new/<id>', delete_news, name='del_new')

]
