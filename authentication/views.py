from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def signUp(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        org = request.POST.get('org')
        password = request.POST.get('password')

        newUser = User.objects.create_user(username=username, email=email, password=password, org=org)
        newUser.save()

        return redirect('login')


    return render(request, 'auth/reg.html')




def singIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('customer_Info')  # Ensure 'index' is defined in your URLs
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'auth/login.html')



def logout_user(request):

    logout(request)

    return redirect('login')


def forget_password(request):
    
    return render(request,'auth/forget.html')

