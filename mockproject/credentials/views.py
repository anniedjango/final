
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from credentials.forms import SignUpForm


# Create your views here.
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password,)

        if user is not None:
            auth.login(request,user)
            return redirect('but')
        else:
            messages.info(request,"invaild credentials")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method==  'POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken please fill the field")
                return redirect('register')
            if username =="":
                messages.info(request, " please fill the field")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)


                user.save()
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')


    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request,"index.html")
def but(request):
    return render(request,"button.html")
def form(request):
    return render(request,"form.html")


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save

    else:
        form = SignUpForm()





    return render(request, 'signup.html', {'form': form})





def acp(request):



 return render(request,"accept.html")