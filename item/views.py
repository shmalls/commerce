from django.shortcuts import render
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
	if request.method == 'GET':
		itemId = request.GET.get('id')
		#cart = request.session.get('cart', {})
		item = Item.objects.get(pk=itemId)
		cart = Cart(request)
		#quant = cart.get('itemId', 0)
		#cart[itemId] = quant+1
		#request.session['cart'] = cart
		cart.add(item, item.price, 1)
		message = "Added " + item.name + " to cart"
		return render(request, 'cart.html', {'message' : message, 'cart' : cart})
	return HttpResponse("bad")