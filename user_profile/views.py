from django.shortcuts import render
from .models import *

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
