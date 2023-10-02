from .models import *
import django_filters

class JobFilter(django_filters.FilterSet):
    # salary = django_filters.RangeFilter()
    
    class Meta:
        model = Job
        fields = {
                'title': ['icontains'], 
                'catagory': ['icontains'],
                'salary': ['lt','gt'],
                'locations': ['icontains']
            }
        
class JobseekerFilter(django_filters.FilterSet):
    # salary = django_filters.RangeFilter()
    
    class Meta:
        model = Jobseeker
        fields = {
                'mobile',
                'user',
            }