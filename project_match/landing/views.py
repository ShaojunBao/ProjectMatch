from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateAppUserForm
from django.contrib.auth import authenticate
from . import models
def index(request):
    return render(request, 'landing/index.html')

def login(request):
    if request == 'POST':
        username = request.POST['email']
        print(username)
        password = request.POST['password']
        user = authenticate(username, password)
        if user is not None:
            return render(request, 'landing/index.html')
    return render(request, 'landing/login.html')
    
def signup(request, form=None, signup_errors=None):
    if request.method == 'POST':
        user_form = CreateAppUserForm(request.POST)
        if user_form.is_valid():
            user_form.save() 
            print(user_form)
            return render(request, 'landing/registerprofile.html', {'user' : user_form})
        else:
            #Return page with signup_errors
            signup_errors = user_form.errors.as_text()
            form = user_form
            return render(request, 'landing/signup.html', {'form': form, 'signup_errors': signup_errors}) #Render with signup_errors
    else:
        form = CreateAppUserForm()
        return render(request, 'landing/signup.html', {'form': form})

def registerprofile(request):
    user = models.AppUser.objects.filter(username = 'xzhang1206@gmail.com')[0]
    return render(request,'landing/registerprofile.html', {'user' : user})
    

