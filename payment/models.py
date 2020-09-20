from django.contrib.gis.db import models
from django.conf import settings

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="customer", on_delete=models.CASCADE)
    customerid = models.CharField(max_length=255)
    graphql_id = models.CharField(max_length=255)
    company = models.CharField(max_length=50, blank=True, null=True)   
    email = models.EmailField()
    fax = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    merchant_id = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)   
    website = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, related_name="transaction", on_delete=models.CASCADE)
    transactionid = models.CharField(max_length=255)
    graphql_id = models.CharField(max_length=255)
    amount = models.FloatField()
    authorization_expires_at = models.CharField(max_length=255, blank=True, null=True)
    currency_iso_code = models.CharField(max_length=10, blank=True, null=True)
    cvv_response_code = models.CharField(max_length=10, blank=True, null=True)
    discount_amount = models.FloatField(blank=True, null=True)
    gateway_rejection_reason = models.CharField(max_length=255, blank=True, null=True)
    master_merchant_account_id = models.CharField(max_length=255, blank=True, null=True)
    merchant_account_id = models.CharField(max_length=255, blank=True, null=True)
    network_response_code = models.CharField(max_length=255, blank=True, null=True)
    network_response_text = models.CharField(max_length=255, blank=True, null=True)
    network_transaction_id = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.CharField(max_length=255, blank=True, null=True)
    payment_instrument_type = models.CharField(max_length=255, blank=True, null=True) 
    plan_id = models.CharField(max_length=255, blank=True, null=True) 
    processor_authorization_code = models.CharField(max_length=255, blank=True, null=True) 
    processor_response_code = models.CharField(max_length=255, blank=True, null=True) 
    processor_response_text = models.CharField(max_length=255, blank=True, null=True)
    processor_settlement_response_code = models.CharField(max_length=255, blank=True, null=True)
    processor_settlement_response_text = models.CharField(max_length=255, blank=True, null=True)
    retrieval_reference_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    transaction_type = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class CreditCardDetails(models.Model):
    transaction = models.OneToOneField(Transaction, related_name="credit_card", on_delete=models.CASCADE)
    token = models.CharField(max_length=255, blank=True, null=True)
    binnumber = models.PositiveIntegerField()
    last_4 = models.PositiveIntegerField()
    card_type = models.CharField(max_length=50)
    expiration_month = models.PositiveIntegerField()
    expiration_year = models.PositiveIntegerField()
    customer_location = models.CharField(max_length=5)
    cardholder_name = models.CharField(max_length=50, blank=True, null=True)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class StatusHistory(models.Model):
    transaction = models.OneToOneField(Transaction, related_name="status_history", on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    amount = models.FloatField()
    user = models.CharField(max_length=50)
    transaction_source = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        