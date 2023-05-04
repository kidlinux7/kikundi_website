from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import json
from django.template import RequestContext
from closeio_api import Client
import closeio_api



def home(request):
    # Get Api Key
    # api = Client('api_7K2YhS8FvSzMeqHX85ExIN.7KKsiATSjW9acEe8YfJJOw')
    
    # opportunity_list = api.get('opportunity', params={'_order_by': '-date_updated', '_limit': 5})
    # print(opportunity_list)

    # post a lead
    # available_lead = api.post('lead', data={'name': 'Test Lead from django'})

    # lead_results = api.get('lead',params={'display_name':'Ivan David'})
    # print(lead_results)

    


    if request.method == 'POST':
        if 'demoButton' in request.POST:
            # Obtained variables
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            company_name = request.POST['company_name']
            title = request.POST['title']
            email = request.POST['email']
            phone = request.POST['phone']
            subject = request.POST['subject']
            message = request.POST['message']


            # Adding the lead to the Closeio dashboard
            api = Client('api_7K2YhS8FvSzMeqHX85ExIN.7KKsiATSjW9acEe8YfJJOw')
            available_lead = api.post('lead', data={'name': first_name+' '+last_name,'title':title,'company':company_name,'message':message})
            demo = Demo.objects.create(first_name = first_name,last_name = last_name,company = company_name,title = title,email=email,phone=phone,subject=subject,message=message)
            demo.save()
            messages.info(request,'Thank you, your information has been received')

        # if 'subscriberEmailButton' in request.POST:
        #     email = request.POST['subscriberEmail']
        #     our_subscriber = Subscriber.objects.create(email=email)
        #     our_subscriber.save()
        #     messages.info(request,'Thank you, your information has been received')
        # return redirect('home')


        return redirect('home')
    else:
        context = {}


    return render(request, 'index.html')



def moses(request):
    return render(request,'moses.html')

def termsandcondition(request):
    return render(request,'termsandcondition.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def test(request):
    return render(request,'test.html')