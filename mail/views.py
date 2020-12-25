from django.shortcuts import HttpResponse,render
from django.core.mail import EmailMessage
import random

def mailSend(request):
    if request.method=='POST':
        otp  = random.randrange(1111,9999)
        mess = f"your OTP is {otp}"
        email = EmailMessage('WELCOME TO MOHIT_CITY',mess, to=['my73811@gmail.com'])
        email.send()

        print("mail sended.......")
        return HttpResponse("your mail sended")
    return render(request,'index.html')
