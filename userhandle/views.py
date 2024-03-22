from django.http import HttpResponse
from userhandle.models import Client
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User 


# Create your views here.


def welcome_email(request):
    email = request.GET.get("email", None)
    if email == None:
        return HttpResponse("please provide email")
    # get client data from the Client model 
    # draft a welcome email with welcome email template 
    # send mail 
    return HttpResponse(f"{email}")

def client_login(request):
    
    if request.method == 'POST':

        # Get email and password from the POST request
        email = request.POST['email']
        password = request.POST['password']

        # Find the user by email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            # Authenticate the user using email and password
            user = authenticate(request, username=user.username, password=password)

            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                return redirect('index')  # Redirect to a dashboard or profile page
            else:
                # Authentication failed, show an error message
                messages.error(request, 'Invalid login credentials. Please try again.')
                return HttpResponse('Invalid login credentials. Please try again.')
        else:
            # User with the given email does not exist, show an error message
            messages.error(request, 'User with this email does not exist.')
            return HttpResponse('User with this email does not exist.')

    return render(request, 'client_login.html')  # Render the 


def client_registration(request):
    return render(request, "client_registration.html")


def client_logout(request):
    logout(request)
    return redirect("index")






