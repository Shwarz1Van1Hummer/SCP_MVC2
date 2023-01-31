from django.shortcuts import render
from django.views.generic import ListView
from bank.models import Account, Card


class AccoutView(ListView):
    model = Account
    template_name = 'main_work/profile.html'
    context_object_name = 'account'
    extra_context = {'owner':Account.owner}

