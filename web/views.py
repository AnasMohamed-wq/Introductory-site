from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.mail import EmailMessage

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
        # 1. سحب البيانات من الفورم
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_email = request.POST.get('email') # إيميل الزائر
        message_content = request.POST.get('message')

        # 2. تجهيز محتوى الرسالة التي ستصلك
        subject = f"New Inquiry from {first_name} {last_name}"
        body = (
            f"You have a new inquiry from your website:\n\n"
            f"Name: {first_name} {last_name}\n"
            f"Visitor Email: {user_email}\n\n"
            f"Message:\n{message_content}"
        )

        # 3. إعداد الإيميل (الإرسال والاستقبال بنفس الإيميل)
        email_sender = 'anas.moh0147@gmail.com' # إيميل النظام
        email_receiver = ['anas.moh0147@gmail.com'] # الإيميل المستلم

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=email_sender,
            to=email_receiver,
            reply_to=[user_email], # تفعيل إمكانية الرد المباشر على الزائر
        )

        try:
            email.send(fail_silently=False)
            messages.success(request, _("Your message has been sent successfully!"))
        except Exception as e:
            # طباعة الخطأ في الكونسول للتصحيح أثناء التطوير
            print(f"Mail Error: {e}") 
            messages.error(request, _("An error occurred. Please try again later."))

        return redirect('contact')
    
    return redirect('contact')




