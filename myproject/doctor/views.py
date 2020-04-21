# from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .serializers import DoctorSerializer,d_experienceSerializer
# from django.db.models import Q
# from doctor.models import doctor,d_experience
# from django.contrib import messages


# Create your views here.

	# def search(request):
	# if request.method =='POST':
	# 	srch = request.POST['search']
	# 	# pk = request.POST('pk')
	# 	# queryset = doctor.objects.filter(user_id = pk)
	# 	# if not queryset:
	# 	# 	return Response([])
	# 	# else:
			

	# 	if srch:
	# 		match = doctor.objects.filter(Q(first_name__icontains=srch) | 
	# 									   Q(city__icontains=srch))

	# 		if match:
	# 			return render(request,'search.html',{'doc':match})
	# 		else:
	# 			messages.error(request,'no result found')
	# 	else:
	# 		return HttpResponseRedirect('/search/')

	# return render(request,'search.html')
