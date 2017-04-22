from django.shortcuts import render
from item.models import Item
from cart.cart import Cart
from commerce.forms import SearchForm
from django.forms.formsets import formset_factory
from cartapp.forms import *



# Create your views here.
def search(request):
  cart = Cart(request)
  search = request.GET.get('search')
  items = Item.objects.filter(name__icontains=search)
  itemList = []
  total = 0
  for item in cart:
    itemList.append(item)
    total += item.total_price
  print(itemList)
  CartFormSet = formset_factory(CartForm, extra=0)
  if request.method == "POST" and len(itemList) > 0:
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
    return render(request,"search.html",{
      's_form':SearchForm(), 
      'cart' : cart, 
      'formset' : formset, 
      'total' : total,
      'user' : request.user,
      'items' : items,
      'search' : search,
      })
  else:
    formset = CartFormSet(initial=[{'itemId' : item.object_id,
      'quantity' : item.quantity, 'name' : item.product.name, 'total_price' : item.total_price} for item in cart])
    message = 'Your Cart'
  return render(request,"search.html",{
  	's_form':SearchForm(), 
  	'cart' : cart, 
  	'formset' : formset, 
  	'total' : total,
  	'user' : request.user,
  	'items' : items,
  	'search' : search,
  	})

#	form = SearchForm();
#	if request.method == 'GET':
#		search = request.GET.get('search')
#		items = Item.objects.filter(name__icontains=search)
#		return render(request,'search2.html',{'items' : items, 'form' : form})
#	else:
#		form = SearchForm();
#	return render(request,"base.html",{'form':form})