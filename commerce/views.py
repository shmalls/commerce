from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.postgres.search import SearchVector

def index(request):
	if request.method == 'POST':
		return HttpResponse("SERCH")
	context = {}
	return render(request,"base.html",{})

#def search(request):
#	if request.method == 'POST':
#		return HttpResponse("SERCH")