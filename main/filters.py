import django_filters
from expads.models import Expatad

class Expatadfilter(django_filters.FilterSet):
    price=django_filters.RangeFilter()
    fullname = django_filters.CharFilter(lookup_expr='icontains')
    Description = django_filters.CharFilter(lookup_expr='icontains')
    landmark = django_filters.CharFilter(lookup_expr='icontains')
    city = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model : Expatad
        fields = {
            'fullname' : ['icontains'],
            'Description' : ['icontains'],
            'landmark' : ['icontains'],
            'city' : ['icontains'],
            #'price': ['lt','gt'],
        }


