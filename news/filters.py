from django_filters import FilterSet, DateFilter, ModelChoiceFilter
from django.forms.widgets import DateInput
from .models import Post, Category

class PostFilter(FilterSet):
    date = DateFilter(widget=DateInput(attrs={'type': 'date'}))
    category = ModelChoiceFilter(field_name='category', queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'category': ['exact'],
        }
