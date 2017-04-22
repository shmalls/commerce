from django.shortcuts import render, render_to_response, redirect, HttpResponseRedirect
from django.http import HttpResponse
from item.models import *
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .forms import SearchForm, LoginForm, RegistrationForm
from user_profile.models import Profile
from cart.cart import Cart
from django.forms.formsets import formset_factory
from cartapp.forms import *


def index(request):
  cart = Cart(request)
  itemList = []
  total = 0
  for item in cart:
    itemList.append(item)
    total += item.total_price
  print(itemList)
  CartFormSet = formset_factory(CartForm, extra=0)
  if request.method == "POST" and len(itemList) > 0:
    formset = CartFormSet(request.POST)

    if(formset.is_valid()):
      index = 0
      for form in formset:
        item = Item.objects.get(pk=itemList[index].object_id)
        cart.update(item,form.cleaned_data['quantity'],itemList[index].unit_price)
        index += 1
    else:
      print (formset.errors)
    cart = Cart(request)
    total = 0
    for item in cart:
      total += item.total_price
    formset = CartFormSet(initial=[{'itemId' : item.object_id,
      'quantity' : item.quantity, 'name' : item.product.name, 'total_price' : item.total_price} for item in cart])
    message = 'Your Cart'
    return render(request,"index.html",{
      's_form':SearchForm(), 
      'cart' : cart, 
      'formset' : formset, 
      'total' : total,
      'user' : request.user
      })
  else:
    formset = CartFormSet(initial=[{'itemId' : item.object_id,
      'quantity' : item.quantity, 'name' : item.product.name, 'total_price' : item.total_price} for item in cart])
    message = 'Your Cart'
  return render(request,"index.html",{'s_form':SearchForm(), 'cart' : cart, 'formset' : formset, 'total' : total})

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
          return redirect('/register/')
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
            user.save()
            return redirect('/login/')
        else:
        	#user cannot be created
        	return render(request, 'register.html',{'form' : form})
    #not post, load register
    else:
    	form = RegistrationForm()
    	return render(request, 'register.html', {'form' : form})