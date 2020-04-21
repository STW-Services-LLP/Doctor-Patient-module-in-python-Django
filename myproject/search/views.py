# from django.shortcuts import render

from itertools import chain
# from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from search.models import patient
from doctor.models import doctor 
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.models import UserManager
from django.shortcuts import redirect
# from rest_framework import generics
# from search.filters import SearchFilter	


# # Create your views here.
def home(request):
	return render(request,"index.html",{})


class SearchView(ListView):
	template_name = 'search.html'
	# paginate_by = 20
	count = 0
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['count'] = self.count or 0
		context['query'] = self.request.GET.get('search',None)
		return context

	def get_queryset(self):
		request = self.request
		query = request.GET.get('search')
		
		if query is not None:
			patient_results        = patient.objects.search(query)
			doctor_results      = doctor.objects.search(query)
			# profile_results     = Profile.objects.search(query)
			
			# combine querysets 
			queryset_chain = chain(
					patient_results,
					doctor_results,
					# profile_results
			)        
			qs = sorted(queryset_chain, 
						key=lambda instance: instance.pk, 
						reverse=True)
			self.count = len(qs) # since qs is actually a list
			return qs
			return patient.objects.none() # just an empty queryset as default


# class SearchViewResult(generics.ListApiView):
# 	serializer_class = PatientSerializers
# 	queryset = patient.objects.all()
# 	filter_backends = (SearchFilter)
# 	search_fields = ('name','city','department')