from django.shortcuts import render, redirect
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def purchase(request):
	if request.method == 'GET':
		if request.user.is_authenticated():
			cart = Cart(request)
			return render(request, 'checkout.html', {'ship_form' : ShippingForm(), 'pay_form' : PaymentForm()})
		else:
			return redirect('/login/')
	if request.method == 'POST':
		if request.user.is_authenticated():
			cart = Cart(request)
			cart.new(request)
			return render(request, 'ordercomplete.html' , {})