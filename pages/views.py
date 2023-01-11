from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import json
from django.template import RequestContext


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        subject = request.POST['subject']
        message = request.POST['message']

        contact_us = Contact_us.objects.create(name = name,email=email,phone_number=phone_number,subject=subject,message=message)
        contact_us.save()
        messages.info(request,'Thank you, your information has been received')
        return redirect('home')
    else:
        context = {}


    return render(request, 'index.html')