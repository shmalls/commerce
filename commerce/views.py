from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from item.models import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .forms import SearchForm, LoginForm, RegistrationForm

def index(request):
	form = SearchForm();
	return render(request,"base.html",{'form':form})

def login(request):
  if request.method == 'POST':
      form = LoginForm(request.POST)
      if form.is_valid():
          user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
          if user is not None:
              if user.is_active:
                  auth_login(request, user)
                  form = SearchForm();
                  return render(request, 'base.html',{ 'user': request.user, 'form' : form})
          #not active user, redirect to register
          form = RegistrationForm()
          return render(request, 'register.html', {'form' : form})
  #not post, load login
  form = LoginForm()
  return render(request, 'login.html', {'form' : form})

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            loginform = SearchForm()
            return render(request, 'base.html',{'form' : loginform})
    else:
    	form = RegistrationForm()

    	return render(request, 'register.html', {'form' : form})