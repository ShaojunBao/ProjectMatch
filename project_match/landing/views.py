from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
import smtplib
from . import models
def index(request):
    return render(request, 'landing/index.html')

def login_screen(request):
    return render(request, 'landing/login.html')

#RESTful API - GET, POST
def login(request):   
    username = request.POST['email']
    password = request.POST['password']
    if models.AppUser.objects.filter(email=username, password=password).exists():
        return render(request, 'landing/landing.html')
    return render(request, 'landing/login.html', 
    {'message' : 'Please enter a valid username and password to login'})

def register(request):
    return render(request, 'landing/signup.html')

def signup(request):   
    cur_email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    
    if models.AppUser.objects.filter(email=cur_email).exists():
        message = "The email has already been registered"
        return render(request, "landing/signup.html", {"message": message})
    if password1 != password2:
        message = "The password you entered doesn't match"
        return render(request, "landing/signup.html", {"message": message})
    # TO-DO check if the password meets security requirements and send message back to front-end
    # at least 8 characters long, contains at least one captial letter, one lower case letter and one special character
    appUser = models.AppUser(email=cur_email, password=password1, firstname=firstname, lastname=lastname)
    smtplibObject = smtplib.SMTP("smtp.gmail.com", 587)
    smtplibObject.ehlo()
    smtplibObject.starttls()
    # replace the app password for gmail under google account -> security -> Signing in to Google -> choose mail and generate app password
    smtplibObject.login("mulesoft.vcores.monitoring@gmail.com", "oerhjpdurgtxuobr")
    sendText="Subject: Welcome to Project Match\n"
    sendText += firstname+", \n\n"
    sendText += "For security purposes, this automatic email has been sent because a new account has been registered on Project Match with this email. If you made this request, you do not need to do anything further.\n"
    sendText += "If you did not initiate this request, please contact Project Match admin xzhang1206@gmail.com for further support. "
    appUser.save()
    smtplibObject.sendmail("mulesoft.vcores.monitoring@gmail.com", cur_email, sendText)
    message = "Your account has been created"
    return render(request, "landing/login.html", {"message": message } )

         

    

