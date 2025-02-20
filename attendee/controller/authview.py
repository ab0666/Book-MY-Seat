from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from attendee.forms import CustomUserForm

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Register Successfully! Login to Continue")
            return redirect('/login')
    context = {'form': form}
    return render(request, "attendee/auth/register.html", context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already loggedin")
        return redirect('/')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwp = request.POST.get('password')
            user = authenticate(request, username=name, password=passwp)
            if user is not None:
                login(request, user)
                messages.success(request, "logged in Sucessfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect('/login')    
        return render(request, "attendee/auth/login.html")
    
def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Sucessfully")
    return redirect('/')

