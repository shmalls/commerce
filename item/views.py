from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Review, ReviewForm
from cart.cart import Cart
from django.shortcuts import get_object_or_404

# Create your views here.
def item(request):
	if request.method == 'GET':
		itemId = request.GET.get('id')
		try:
			reviews = Review.objects.filter(itemId=itemId)
			print("found Reviews")
		except Review.DoesNotExist:
			reviews = None
		item = Item.objects.get(pk=itemId)
		
		reviewForm = ReviewForm(initial={'itemId':itemId, 'user':request.user})
		
		return render(request, 'item.html', {'item' : item, 'reviews' : reviews, 'reviewForm' : reviewForm})
		
	elif request.method == 'POST':
		itemId = request.GET.get('id')
		reviewForm = ReviewForm(request.POST)
		print(request.POST)
		
		new_review = reviewForm.save()
	#	item = Item.objects.get(pk=itemId)
	#	review = Review(request)
	#	review.add(
		
		return redirect('/item/?id='+itemId)
	
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
	
# this isn't currently used
def add_review(request):
	if request.method == 'POST':
		itemId = request.GET.get('id')
		user = request.user
		reviewForm = ReviewForm(request.POST)
		
		new_review = reviewForm.save()
	#	item = Item.objects.get(pk=itemId)
	#	review = Review(request)
	#	review.add(
		
		return HttpResponse("Review Submitted")
	return HttpResponse("No Review Submitted")