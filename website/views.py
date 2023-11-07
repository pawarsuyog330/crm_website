from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    # check to see if user is logged in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # authenticate user details
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User logged in successfully!')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username or password. Please try again.')
            return redirect('home')
    else:
        return render(request, 'home.html', locals())


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')


def register(request):
    return render(request, 'register.html', locals())
