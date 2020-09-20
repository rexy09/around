from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(Customer)
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "user", "customerid", "first_name", "last_name", "email"]
    list_display_links = ["pk", "user"]
    

@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "customer", "transactionid", "amount"]    
    list_display_links = ["pk", "customer"]
    

@admin.register(CreditCardDetails)
class CreditCardDetailsModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "transaction", "binnumber", "last_4", "card_type"]
    list_display_links = ["pk", "transaction"]

     
@admin.register(StatusHistory)
class StatusHistoryModelAdmin(admin.ModelAdmin):
    list_display = ["pk", "transaction", "status", "amount", "user", "transaction_source"]
    list_display_links = ["pk", "transaction"]