from .models import Contact
from django.shortcuts import render ,  HttpResponse, redirect
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def error_404_view(request , exception):
    return render(request, '404.html')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message =request.POST['message']
        if len(name)<2 or len(email)<3 or len(message)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, message=message)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "index.html")