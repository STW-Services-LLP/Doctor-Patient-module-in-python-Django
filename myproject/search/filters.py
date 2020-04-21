import django_filters
from django import forms
from search.models import patient


# class SearchFilter(django_filters.FilterSet):

# 	name = django_filters.CharFilter(lookup_expr = icontains)
# 	city = django_filters.CharFilter(lookup_expr = icontains)
# 	department = django_filters.CharFilter(lookup_expr = icontains)

# 	class Meta:
# 		model = patient
# 		fields = {
# 			'name':['icontains'],
# 			'city':['icontains'],
# 			'department':['icontains'],
# 			}