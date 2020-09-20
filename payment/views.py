from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json
import os
from .models import *
from post.models import *
from django.http import HttpResponse




@login_required
def payment_view(request, *args, **kwargs):
    #generate all other required data that you may need on the #checkout page and add them to context.
    user = request.user
    postid = kwargs['post']
    planid = kwargs['plan']
   
    context = {
        
        'postid':postid,
        'planid':planid,
        }
    return render(request, 'payment.html', context)


@login_required
def checkout(request, *args, **kwargs):
    if request.method == 'POST':
       
        plan_id = request.POST.get('planid', None)
        post_id = int(request.POST.get('postid', None))
        
        post = Post.objects.get(id=post_id)
        print(post)
       
     
               
        # try:
        #     # Existing Customer
        #     client = Customer.objects.get(user=request.user)
        # except Customer.DoesNotExist:
        #     # New Customer
        #     client = Customer.objects.create(
        #     user=request.user, 
        #     customerid=customer_create.customer.id,
        #     graphql_id=customer_create.customer.graphql_id,
        #     company=customer_create.customer.company,
        #     email=customer_create.customer.email,
        #     fax=customer_create.customer.fax,
        #     first_name=customer_create.customer.first_name,
        #     last_name=customer_create.customer.last_name,
        #     merchant_id=customer_create.customer.merchant_id,
        #     phone=customer_create.customer.phone,
        #     website=customer_create.customer.website            
        #     )
        
        if plan_id == '1':
                                    
            if post:
                sponsored = SponsoredPost.objects.filter(post=post).update(sponsored=True, plan=7)
                print("Updated: " + str(sponsored))
                
                if sponsored == 0:
                    sponsored = SponsoredPost.objects.create(post=post, sponsored=True, plan=7)
                    print("Created: "+str(sponsored))
                    
        elif plan_id == '2':
                                   
            if post:
                sponsored = SponsoredPost.objects.filter(post=post).update(sponsored=True, plan=30)
                print("Updated: " + str(sponsored))
                
                if sponsored == 0:
                    sponsored = SponsoredPost.objects.create(post=post, sponsored=True, plan=30)
                    print("Created: "+str(sponsored))
        elif plan_id == '3':
                                  
            if post:
                sponsored = SponsoredPost.objects.filter(post=post).update(sponsored=True, plan=60)
                print("Updated: " + str(sponsored))
                
                if sponsored == 0:
                    sponsored = SponsoredPost.objects.create(post=post, sponsored=True, plan=60)
                    print("Created: "+str(sponsored))
        else:
            print("Invalid plan")            
       
        
        
        # transact = Transaction.objects.create(
        #     customer=client,
        #     transactionid=result.transaction.id,
        #     graphql_id=result.transaction.graphql_id,
        #     amount=result.transaction.amount,
        #     authorization_expires_at=result.transaction.authorization_expires_at,
        #     currency_iso_code=result.transaction.currency_iso_code,
        #     cvv_response_code=result.transaction.cvv_response_code,
        #     discount_amount=result.transaction.discount_amount,
        #     gateway_rejection_reason=result.transaction.gateway_rejection_reason,
        #     master_merchant_account_id=result.transaction.master_merchant_account_id,
        #     merchant_account_id=result.transaction.merchant_account_id,
        #     network_response_code=result.transaction.network_response_code,            
        #     network_response_text=result.transaction.network_response_text,
        #     network_transaction_id=result.transaction.network_transaction_id,
        #     order_id=result.transaction.order_id,
        #     payment_instrument_type=result.transaction.payment_instrument_type,
        #     plan_id=result.transaction.plan_id,
        #     processor_authorization_code=result.transaction.processor_authorization_code,
        #     processor_response_code=result.transaction.processor_response_code,
        #     processor_response_text=result.transaction.processor_response_text,
        #     processor_settlement_response_code=result.transaction.processor_settlement_response_code,
        #     processor_settlement_response_text=result.transaction.processor_settlement_response_text,
        #     retrieval_reference_number=result.transaction.retrieval_reference_number,
        #     status=result.transaction.status,
        #     transaction_type=result.transaction.type                    
        # )
        
        # card = CreditCardDetails.objects.create(
        #     transaction=transact,
        #     token=result.transaction.credit_card_details.token,
        #     binnumber=result.transaction.credit_card_details.bin,
        #     last_4=result.transaction.credit_card_details.last_4,
        #     card_type=result.transaction.credit_card_details.card_type,
        #     expiration_month=result.transaction.credit_card_details.expiration_month,
        #     expiration_year=result.transaction.credit_card_details.expiration_year,
        #     customer_location=result.transaction.credit_card_details.customer_location,
        #     cardholder_name=result.transaction.credit_card_details.cardholder_name,
        #     image_url=result.transaction.credit_card_details.image_url
        # )
        
        # status = StatusHistory.objects.create(
        #     transaction=transact,
        #     status=result.transaction.status_history[0].status,
        #     amount=result.transaction.status_history[0].amount,
        #     user=result.transaction.status_history[0].user,
        #     transaction_source=result.transaction.status_history[0].transaction_source
        # )
        
        
    return HttpResponse('Ok')




