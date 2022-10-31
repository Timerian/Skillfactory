import django_filters
from django.forms import DateTimeInput
from django_filters import FilterSet

from .models import Post


class PostFilter(FilterSet):
    time_add = django_filters.DateTimeFilter(field_name='time_add', lookup_expr='gt',
                                             widget=DateTimeInput(
                                                 format='%Y-%m-%d %H:%M',
                                                 attrs={'type': 'datetime-local'},),
                                             )

    class Meta:
        model = Post
        fields = {
            'head': ['icontains'],
            'categories': ['exact'],
            'type': ['exact']
        }
