import django_filters
from django_filters import DateFilter, CharFilter

from .models import Post


class PostFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="created",
                            lookup_expr='gte')
    end_date = DateFilter(field_name="created",
                          lookup_expr='lte')

    title = CharFilter(field_name="title",
                       lookup_expr="icontains")

    class Meta:
        model = Post
        fields = ['author', ]
