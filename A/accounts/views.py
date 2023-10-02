from django.shortcuts import render , redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages

def alll (request):
    return render(request, 'register.html')
def user_register(request):
    if request.method == 'post' :
        form = UserRegistrationForm(request.post)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            User.first_name = cd['first_name']
            User.last_name = cd['last_name']
            User.save()
            messages.success(request, 'user registerd successfuly ' , 'success')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html' , {'form' : form})

