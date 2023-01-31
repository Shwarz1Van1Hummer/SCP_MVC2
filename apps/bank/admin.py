from django.contrib import admin
from bank.models import Card, Transactions, Account


@admin.register(Card)
class CardsAdmin(admin.ModelAdmin):
    pass


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountsAdmin(admin.ModelAdmin):
    pass