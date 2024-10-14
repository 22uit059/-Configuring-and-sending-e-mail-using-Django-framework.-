# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'myapp/home.html')

def send_email(request):
    if request.method == 'POST':
        send_mail(
            'Welcome Party - reg.',
            'Greetings!!! Welcome to the Department of Information Technology.',
            settings.EMAIL_HOST_USER,
            ['ksandhiya395@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'myapp/sendMail.html')  # Redirect to sendMail.html after sending the email
    return render(request, 'myapp/home.html')  # Return to home if not POST


