from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from userauths.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def register_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "You have successfully signed up!")
            return redirect("core:index")
    else:
        messages.info(request, "Please fill out the form to sign up.")
    return render (request, 'userauths/sign-up.html', {'form':form})



def login_view(request): 
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.info(request, "Log in Successfull")
            return redirect('core:index')
       
    return render(request, "userauths/sign-in.html")

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out Successfully")
    return redirect('core:index')
