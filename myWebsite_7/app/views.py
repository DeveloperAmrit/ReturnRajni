from django.http import  HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login
import datetime
from .models import video,feedback

def index(request):

    params = {
        "videos" : video.objects.all(),
    }
    return render(request,'index.html',params)

def aboutus(request):
    return render(request,'aboutus.html')
# Login/Signin 
signed_users = []

def showSignIn(request):
    return render(request,'2_signup.html')

def showLogIn(request):
    return render(request,'2_login.html')

def userFeedback(request):
    feedbacker_name = request.GET.get('feedback_name', 'default')
    feedbacker_email = request.GET.get('feedback_email', 'default')
    feedbacker_message = request.GET.get('feedback_message', 'default')
    Current_user = request.user

    _feedback = feedback()
    _feedback.feedbacker = feedbacker_name
    _feedback.feedbacker_email = feedbacker_email
    _feedback.feedback = feedbacker_message
    _feedback.feedbacker_userid = Current_user
    _feedback.save()
    return HttpResponseRedirect('/')


def signIn(request):
    user_name = request.GET.get('name','default')   
    user_email = request.GET.get('email','default')    
    user_password = request.GET.get('password','default')

    # Checking data

    if len(user_name) > 12 or len(user_email) < 4 or user_password == '':
        params = {
            "text" : "Very short email or password \n or Too long name."
        }
        return render(request,'404.html',params)

    signed_users.append(f'{user_email}')
    date = datetime.datetime.now()
    # Creating user
    myuser = User.objects.create_user(user_name,user_email,user_password)
    myuser.last_name = user_name
    myuser.save()
    return HttpResponseRedirect("/")

def logIn(request):
    
    login_name = request.GET.get('login_name')
    login_password = request.GET.get('login_password')
    user = authenticate( username= login_name, password= login_password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        params = {
        "text" : "Email or Password is wrong.Please try again"
        }
        return render(request,'404.html',params)
