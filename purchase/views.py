from django.shortcuts import render, redirect
from cart.cart import Cart
from user_profile.models import *
from item.models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def purchase(request):
	if request.method == 'GET':
		if request.user.is_authenticated():
			cart = Cart(request)
			ship_form = ShippingForm(initial={'first_name':request.user.first_name,
				'last_name':request.user.last_name,'address':request.user.profile.address,
				'city':request.user.profile.city,'state':request.user.profile.state,
				'zip_code':request.user.profile.zip_code})
			pay_form = PaymentForm(initial={'card_number':request.user.profile.card_number,
				'name':request.user.profile.card_name,'exp_date_month':request.user.profile.card_month,
				'exp_date_year':request.user.profile.card_year})
			return render(request, 'checkout.html', {'ship_form' : ship_form, 'pay_form' : pay_form})
		else:
			return redirect('/login/')
	if request.method == 'POST':
		ship_form = ShippingForm(request.POST)
		pay_form = PaymentForm(request.POST)
		cart = Cart(request)
		if ship_form.is_valid() and pay_form.is_valid() and request.user.is_authenticated():
			order = Order.objects.create(
				user=request.user,
				address=ship_form.cleaned_data['address'],
				city=ship_form.cleaned_data['city'],
				state=ship_form.cleaned_data['state'],
				zip_code=ship_form.cleaned_data['zip_code'],
				card_number=pay_form.cleaned_data['card_number'],
				card_name=pay_form.cleaned_data['name'],
				card_month=pay_form.cleaned_data['exp_date_month'],
				card_year=pay_form.cleaned_data['exp_date_year']
				)
			for item in cart:
				itemOrder = ItemOrder.objects.create(
					itemId=Item.objects.get(pk=item.object_id),
					quantity=item.quantity,
					orderId=order)
			cart.new(request)
			items = ItemOrder.objects.filter(orderId=order.pk)
			return render(request, 'ordercomplete.html' , {'order':order,'items':items})