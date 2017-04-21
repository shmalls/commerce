from django.shortcuts import render
import operator
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from purchase.choices import *

# Create your views here.
def profile(request):
	return render(request, 'profile.html', {})

def view_profile(request):
	return render(request,'viewprofile.html',{'first_name':request.user.first_name,
		'last_name':request.user.last_name,'address':request.user.profile.address,
				'city':request.user.profile.city,'state':request.user.profile.state,
				'zip_code':request.user.profile.zip_code})
def edit_profile(request):
	if request.method == 'GET':
		top_form = UserForm(instance=request.user)
		bot_form = ProfileForm(instance=request.user.profile)
		return render(request, 'editprofile.html',{'top_form':top_form, 'bot_form':bot_form})
	elif request.method == 'POST':
		top_form = UserForm(request.POST, instance=request.user)
		bot_form = ProfileForm(request.POST, instance=request.user.profile)
		top_form.save()
		bot_form.save()
		return render(request, 'editprofile.html',{'top_form':top_form, 'bot_form':bot_form})

def view_payment(request):
	return render(request,'viewpayment.html',{'card_number':request.user.profile.card_number,
				'name':request.user.profile.card_name,'card_month':MONTH_CHOICES[request.user.profile.card_month][1],
				'card_year':YEAR_CHOICES[request.user.profile.card_year][1]})

def edit_payment(request):
	if request.method == 'GET':
		pay_form = PaymentForm(instance=request.user.profile)
		return render(request, 'editpayment.html',{'pay_form':pay_form})
	elif request.method == 'POST':
		pay_form = PaymentForm(request.POST,instance=request.user.profile)
		pay_form.save()
		return render(request, 'editpayment.html',{'pay_form':pay_form})

def change_password(request):
	message = ""
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			message = "Your password was successfully updated!"
			return render(request, 'changepassword.html', {'pass_form': form, 'message':message})
		else:
			messages.error(request, 'Please correct the error below.')
			message = "Incorrect password or mismatching passwords"
	else:
		form = PasswordChangeForm(request.user)
	return render(request, 'changepassword.html', {'pass_form': form,'message':message})

def view_orders(request):
	orders = Order.objects.filter(user=request.user)
	orders = sorted(orders, key=operator.attrgetter('pk'), reverse=True)
	return render(request, 'vieworders.html', {'orders':orders})

def order(request):
	if request.method == 'GET':
		orderId = request.GET.get('id')
		order = Order.objects.get(pk=orderId)
		items = ItemOrder.objects.filter(orderId=orderId)
		return render(request, 'order.html', {'order':order,'items':items})