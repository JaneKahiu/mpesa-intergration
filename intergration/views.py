from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django_daraja.mpesa.core import MpesaClient
from requests.exceptions import HTTPError
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    cl = MpesaClient()
    phone_number = 'your phone number' #replace with your phone number
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://api.darajambili.com/express-payment'#replace with your callback url
    #make the stk push request
    try:
        # Make the STK Push request
        response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        
        # Example of handling response attributes
        if response.response_code == '0':  # '0' usually indicates success in M-Pesa API
            return HttpResponse("STK Push initiated successfully!")
        else:
            error_message = response.error_message if response.error_message else 'STK Push failed'
            return HttpResponse(f"STK Push failed: {error_message}", status=400)

    except Exception as e:
        # Handle any exceptions that may occur
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

@csrf_exempt
def stk_push_callback(request):
    # Handle the callback logic here
    return JsonResponse({"ResultCode": 0, "ResultDesc": "Success"})

