from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.postgres.search import SearchVector
from item.models import *
from .forms import *
def index(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			print (form.cleaned_data['search'])
			items = Item.objects.filter(name__icontains=form.cleaned_data['search'])
			print (items)
			return render_to_response('search.html',{'items' : items})
	else:
		form = SearchForm();
	return render(request,"base.html",{'form':form})

#def search(request):
#	if request.method == 'POST':
#		return HttpResponse("SERCH")