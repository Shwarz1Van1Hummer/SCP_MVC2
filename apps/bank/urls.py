from django.urls import path
from apps.bank.views import AccoutView

urlpatterns = [
    path('profile/', AccoutView.as_view(), name='profile')

]