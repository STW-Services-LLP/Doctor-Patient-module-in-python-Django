# from django.shortcuts import render


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from search.models import patient
from django.contrib import messages


# # Create your views here.
def home(request):
	return render(request,"index.html",{})

def search(request):
	if request.method =='POST':
		srch = request.POST['search']

		if srch:
			match = patient.objects.filter(Q(name__icontains=srch) | 
										   Q(city__icontains=srch))

			if match:
				return render(request,'search.html',{'sr':match})
			else:
				messages.error(request,'no result found')
		else:
			return HttpResponseRedirect('/search/')

	return render(request,'search.html')
				
