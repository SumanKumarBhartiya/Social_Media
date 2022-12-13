from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.

def Login_View(request):
    if request.method=="POST":
        # Get the post parameters
        uname=request.POST['uname']
        pwd=request.POST['pwd']

        user=authenticate(username= uname, password= pwd)
        if user is not None:
            login(request, user)
            return redirect('Home')

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("Login_View")
    else:
        return render(request,"login.html")


def Signup_View(request):
    if request.method=="POST":
        #GET THE POST PARAMETER
        uname=request.POST['email']
        pwd1=request.POST['pwd1']
        pwd2=request.POST['pwd2']
        name=request.POST['name']
        if(pwd1!=pwd2):
            messages.error(request," Password do not match!! ")
            return redirect('Signup_View')
        else:
            myuser=User.objects.create_user(uname,uname,pwd1)
            myuser.first_name=name
            myuser.save()
            messages.success(request, " Your account has been successfully created")
            return  redirect('Login_View')
    else:
        return render(request,"signup.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('Login_View')

    
@login_required(login_url='Login_View')
def Home(request):
    return render(request,"profile.html")
    