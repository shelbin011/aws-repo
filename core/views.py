from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home(request):
    return render(request, 'core/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
            
    return render(request, 'core/contact.html')
