from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout
from .forms import ProfileForm
# Create your views here.

def Login_View(request):
    if request.method=="POST":
        # Get the post parameters
        uname=request.POST['uname']
        pwd=request.POST['pwd']

        user=authenticate(username= uname, password= pwd)
        if user is not None:
            login(request, user)
            return redirect('News_Feed')

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
        user=User.objects.get(username=uname)
        if(pwd1!=pwd2):
            messages.error(request," Password do not match!! ")
            return redirect('Signup_View')
        elif user is not None:
            messages.error(request,"user exist, login to continue")
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

@login_required(login_url='Login_View')
def News_Feed(request):
    return render(request,'index.html')

def blank(request):
    return render(request,'remove.html')

@login_required(login_url='Login_View')
def EditProfile(request):
    if request.method=="POST":
        #get the post parameter
        profiledata=ProfileForm(request.POST)
        if profiledata.is_valid():
            profiledata.save()
            messages.success(request,"Your profile has been updated!!")
            return redirect('Home')
    else:
        form=ProfileForm()
        return render(request,'editprofile.html',{'form':form})