from django.shortcuts import render, redirect
from django.http import HttpResponse
from new_app.email_spam import email_spam_detection
from new_app.sms_spam import sms_spam_detection
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def spam(request):
    if request.method == 'POST':
        email = request.POST['email']
        sms = request.POST['sms']
        print(email, sms)
    if email != '' and sms == '':
        result = email_spam_detection(email)
    if sms != '' and email == '':
        result = sms_spam_detection(sms)
    if email == '' and sms == '':
        messages.success(
                request, "Enter the email/sms in their respective field once at a time . . .")
        return redirect(index)
    if email !='' and sms !='':
        messages.success(
                request, "Enter the email/sms in their respective field once at a time. . .")
        return redirect(index)
    return render(request,'index.html', {'result': result})