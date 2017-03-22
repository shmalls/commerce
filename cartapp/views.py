from django.shortcuts import render
from cart.cart import Cart
from item.models import *
from .forms import *
from django.forms.formsets import formset_factory

# Create your views here.
def cart(request):
	cart = Cart(request)
	itemList = []
	total = 0
	for item in cart:
		itemList.append(item)
		total += item.total_price
	print(itemList)
	CartFormSet = formset_factory(CartForm, extra=0)
	if request.method == "POST":
		formset = CartFormSet(request.POST)

		if(formset.is_valid()):
			index = 0
			for form in formset:
				item = Item.objects.get(pk=itemList[index].object_id)
				cart.update(item,form.cleaned_data['quantity'],itemList[index].unit_price)
				index += 1
		else:
			print (formset.errors)
		cart = Cart(request)
		total = 0
		for item in cart:
			total += item.total_price
		formset = CartFormSet(initial=[{'itemId' : item.object_id,
			'quantity' : item.quantity, 'name' : item.product.name, 'total_price' : item.total_price} for item in cart])
		message = 'Your Cart'
		return render(request, 'cart.html', {'message' : message, 'cart' : cart, 'formset' : formset, 'total' : total})
	else:
		formset = CartFormSet(initial=[{'itemId' : item.object_id,
			'quantity' : item.quantity, 'name' : item.product.name, 'total_price' : item.total_price} for item in cart])
		message = 'Your Cart'

	return render(request, 'cart.html', {'message' : message, 'cart' : cart, 'formset' : formset, 'total' : total})