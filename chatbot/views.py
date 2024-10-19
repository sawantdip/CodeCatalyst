# chatbot/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'chatbot/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after signup
            return redirect('home')  # Redirect to home after signup
        else:
            # Show form errors if any
            return render(request, 'chatbot/signup.html', {'form': form, 'errors': form.errors})
    else:
        form = UserCreationForm()
    return render(request, 'chatbot/signup.html', {'form': form})


# chatbot/views.py
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Store user ID in session
            request.session['user_id'] = user.id
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'chatbot/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def learn_view(request):
    return render(request, 'chatbot/learn.html') 

def about_view(request):
    return render(request, 'chatbot/about.html')

@login_required
def practice_view(request):
    return render(request, 'chatbot/practice.html')