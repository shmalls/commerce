from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from cart.cart import Cart
from django.shortcuts import get_object_or_404

# Create your views here.
def item(request):
	if request.method == 'GET':
		itemId = request.GET.get('id')
		item = Item.objects.get(pk=itemId)
		return render(request, 'item.html', {'item' : item})
	return HttpResponse("Hello, world. You're at the item index.")

def add_to_cart(request):
	if request.method == 'POST':
		itemId = request.GET.get('id')
		item = Item.objects.get(pk=itemId)
		cart = Cart(request)
		cart.add(item, item.price, 1)
		#message = "Added " + item.name + " to cart"
		return redirect('/cart/')
	#message = ''
	#cart = Cart(request)
	#return render(request, 'cart.html', {'message' : message, 'cart' : cart})