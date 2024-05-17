from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post, Category

class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория'
    )

    added_after = DateTimeFilter(
        field_name='datetime',
        lookup_expr='gt',
        label='Дата',
        widget=DateTimeInput(
            # format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        )
    )

    class Meta:
        model = Post
        label='Название'
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }