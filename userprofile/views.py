from django.shortcuts import render
from django.http import HttpResponse
from item.models import *
from django.contrib.auth.decorators import login_required

@login_required
def userprofile(request):
	return render(request,"userprofile.html",
	{#'user': request.user ,
     #'Jingles': Jingles.objects.filter(user=request.user),
     #'count' : Jingles.objects.filter(user=request.user).count(),
	}

)
@login_required
def editprofile(request):
    user=request.user

    form = EditProfileForm(request.POST or None, initial={'first_name':user.first_name, 'last_name':user.last_name,'email':user.email},)
    if request.method == 'POST':
       if form.is_valid():
          user.first_name = request.POST['first_name']
          user.last_name = request.POST['last_name']
          user.email = request.POST['email']
          user.save()
          return HttpResponseRedirect('%s'%(reverse('userprofile')))

    context = {
        "form": form,
        'Jingles': Jingles.objects.filter(user=request.user),
        'count' : Jingles.objects.filter(user=request.user).count(),

    }

    return render(request, "editprofile.html", context)
