from django.core.mail  import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail  import send_mail
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from .tokens import *



def email_success(email,last_name):
    try:
        template = render_to_string('us_email_template.html', {'name': last_name})
    
        mail = EmailMessage(
            'Thanks for creating an account!',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        mail.fail_silently=False
        mail.send()
    except Exception as e:
        return False
    return True

def email_success_r1(email,last_name):
    try:
        template = render_to_string('rs_email_template.html', {'name': last_name})
    
        mail = EmailMessage(
            'Thanks for creating an account!',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        mail.fail_silently=False
        mail.send()
    except Exception as e:
        return False
    return True

def email_success_r2(email,last_name):
    try:
        template = render_to_string('rs1_email_template.html', {'name': last_name})
    
        mail = EmailMessage(
            'Your account has ben accepted!',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        mail.fail_silently=False
        mail.send()
    except Exception as e:
        return False
    return True

def email_success_r3(email,last_name):
    try:
        template = render_to_string('rs2_email_template.html', {'name': last_name})
    
        mail = EmailMessage(
            'Your account has been rejected!',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        mail.fail_silently=False
        mail.send()
    except Exception as e:
        return False
    return True

def email_delete(email,last_name):
    try:
        template = render_to_string('ud_email_template.html', {'name': last_name})
    
        mail = EmailMessage(
            'Your account has been Deleted!',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        mail.fail_silently=False
        mail.send()
    except Exception as e:
        return False
    return True

def email_delete_r(email,last_name):
    try:
        template = render_to_string('rd_email_template.html', {'name': last_name})
    
        mail = EmailMessage(
            'Your account has been Deleted!',
            template,
            settings.EMAIL_HOST_USER,
            [email],
        )
        mail.fail_silently=False
        mail.send()
    except Exception as e:
        return False
    return True

def job_apply_mail(Uemail,Remail,U_firstName,U_lastName,title):
    try:
        template = render_to_string('job_apply_mail.html', {'Fname':U_firstName,
                                                            'Lname': U_lastName,
                                                            'title': title,
                                                            'Uemail': Uemail,})
    
        mail = EmailMessage(
            'An applicant has applied for a job!',
            template,
            settings.EMAIL_HOST_USER,
            [Remail],
        )
        mail.fail_silently=False
        mail.send()
    except Exception as e:
        return False
    return True

def selectionMail(Uemail,Remail,sub,intromess,mainmess,U_firstName,U_lastName,company):
    try:
        template = render_to_string('selection_mail.html', {'Fname':U_firstName,
                                                            'Lname': U_lastName,
                                                            'intromess':intromess,
                                                            'mainmess':mainmess,
                                                            'company': company,
                                                            'Remail': Remail,})
    
        mail = EmailMessage(
            sub,
            template,
            settings.EMAIL_HOST_USER,
            [Uemail],
        )
        mail.fail_silently=False
        mail.send()
    except Exception as e:
        return False
    return True

# def send_email_token(email,token,last_name):
#     try:
#         template = render_to_string('send_email_token.html', {'name': last_name,'token':token})
    
#         mail = EmailMessage(
#             'Your account needs to be verified.',
#             template,
#             settings.EMAIL_HOST_USER,
#             [email],
#         )
#         mail.fail_silently=False
#         mail.send()
#     except Exception as e:
#         return False
#     return True

# def activateEmail(request,user, email):
#     template = render_to_string('activate_account.html',{
#                                        'user': user.last_name,
#                                        'domain': get_current_site(request).domain,
#                                        'uid': urlsafe_base64_encode(force_bytes(user.username)),
#                                        'token': account_activation_token.make_token(user),
#                                        'protocol':'https' if request.is_secure() else 'http'
#             })
    
#     mail = EmailMessage(
#         'Thanks for creating an account!',
#         template,
#         settings.EMAIL_HOST_USER,
#         [email],
#     )
#     if mail.send():
#         messages.success(request, f"Dear {user}, please go to your email {email} inbox and click on \
#             received activation link to confirm and complete the registration. Note: Check your spam folder.")
#     else:
#         messages.error(request, f'Problen sending email tp {email}, check if you typed it correctly.')

