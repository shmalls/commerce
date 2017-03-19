from django.shortcuts import render
from cart.cart import Cart
from item.models import *
from .forms import *
from django.forms.formsets import formset_factory

# Create your views here.
def cart(request):
	cart = Cart(request)
	itemList = []
	for item in cart:
		itemList.append(item)
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
		formset = CartFormSet(initial=[{'itemId' : item.object_id,
			'quantity' : item.quantity, 'name' : item.product.name} for item in cart])
		message = 'Your Cart'
		return render(request, 'cart.html', {'message' : message, 'cart' : cart, 'formset' : formset})
	else:
		formset = CartFormSet(initial=[{'itemId' : item.object_id,
			'quantity' : item.quantity, 'name' : item.product.name} for item in cart])
		message = 'Your Cart'

	return render(request, 'cart.html', {'message' : message, 'cart' : cart, 'formset' : formset})