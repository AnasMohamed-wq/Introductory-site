from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def courses(request):
    return render(request, 'courses.html')

def vision(request):
    return render(request, 'vision.html' )

def machine(request):
    return render(request, 'machine.html' )

def contact(request):
    return render(request, 'contact.html' )


def a(request):
    return render(request, 't/a.html' )


def index(request):
    return render(request, 't/index.html' )


def h(request):
    return render(request, 't/h.html' )


def about2(request):
    return render(request, 't/about2.html' )


def j(request):
    return render(request, 't/j.html' )



def send_inquiry(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_email = request.POST.get('email')
        message_content = request.POST.get('message')

        full_message = f"Message from: {first_name} {last_name}\nEmail: {user_email}\n\nContent:\n{message_content}"

        try:
            send_mail(
                subject=f"New Inquiry from {first_name}",
                message=full_message,
                from_email='alshlashcompany@gmail.com', # إيميل النظام
                recipient_list=['alshlashcompany@gmail.com'], # الإيميل المستهدف
                fail_silently=False,
            )
            messages.success(request, _("Your message has been sent successfully!"))
        except Exception as e:
            messages.error(request, _("An error occurred. Please try again later."))

        return redirect('contact') # العودة لصفحة التواصل






