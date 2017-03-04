from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def item(request):
	if request.method == 'GET':
		itemId = request.GET.get('id')
		item = Item.objects.get(pk=itemId)
		return render(request, 'item.html', {'item' : item})
	return HttpResponse("Hello, world. You're at the item index.")