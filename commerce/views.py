from django.shortcuts import render
from django.http import HttpResponse
from item.models import *
from .forms import SearchForm
def index(request):
	form = SearchForm();
	return render(request,"base.html",{'form':form})