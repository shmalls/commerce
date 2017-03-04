from django.shortcuts import render
from item.models import Item
from commerce.forms import SearchForm

# Create your views here.
def search(request):
	form = SearchForm();
	if request.method == 'GET':
		search = request.GET.get('search')
		items = Item.objects.filter(name__icontains=search)
		return render(request,'search.html',{'items' : items, 'form' : form})
#	else:
#		form = SearchForm();
#	return render(request,"base.html",{'form':form})