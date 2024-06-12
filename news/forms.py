from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'text']
        

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        category = cleaned_data.get("category")
        title = cleaned_data.get("title")
        
        # if text is not None and len(text) < 20:
        #     raise ValidationError({
        #         "text": "Содержание должно быть не меньше 20 символов."
        #     })
        # elif text is None:
        #     raise ValidationError({
        #         "text": "Заголовок не может быть пустым."
        #     })
        
        # if title is not None and len(title) < 150:
        #     raise ValidationError({
        #         "title": "Заголовок не может быть пустым."
        #     })
        # elif title is None:
        #     raise ValidationError({
        #         "title": "Заголовок не может быть пустым."
        #     })      
          
        # if category is None:
        #     raise ValidationError({
        #         "category": "Вы должны выбрать категорию"
        #     })

        return cleaned_data
    
    # def save(self, commit=True):
    #     post = super().save(commit=False)
    #     post.slug = post.title
    #     if commit:
    #         post.save()
    #     return post