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
              else:
                  return render_to_response('register.html')
          else:
              return render_to_response('register.html')
      else:
          return render_to_response("login.html", {'form' : form})
  form = LoginForm()
  variables = RequestContext(request, {
    'form': form
  })
  return render_to_response("login.html", variables)

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
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'register.html',
    variables,
    )