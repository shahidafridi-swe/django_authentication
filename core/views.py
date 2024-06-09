from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash

from django.contrib import messages
from .forms import RegisterUserForm, UpdateUserProfile

def home(request):
    return render(request, 'home.html')

def registerUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterUserForm()

    return render(request, 'register_form.html', {'form':form, 'type':'Register'})

def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"'{username}' logged in successfully")
                return redirect('profile')
            else:
                messages.error(request, f"'{username}' user not found !!!")
        else:
            try:
                User.objects.get(username=username)
                messages.error(request, "Your Password is incorrect !!!")
            except:
                messages.error(request, f"'{username}' user not found !!!")
    else:
        form = AuthenticationForm()           
    return render(request, 'register_form.html',{'form':form, 'type':'Login'})

# @login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request, 'Logout successfull !!!')
    return redirect('login')

def profileUser(request):
    return render(request, 'profile.html')

def updateProfileUser(request):
    if request.method == "POST":
        form = UpdateUserProfile(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account updated successfully for {username}!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UpdateUserProfile(instance=request.user)
    return render(request, 'register_form.html', {'form':form, 'type':'Update Profile'})


def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully!!!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'register_form.html',{'form':form, 'type':'Change Password'})


def setPassword(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully!!!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'register_form.html',{'form':form, 'type':'Change Password'})