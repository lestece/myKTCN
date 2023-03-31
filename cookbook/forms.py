from django import forms
from django.forms import ModelForm, Textarea
from .models import Recipe, Comment
from django_summernote.widgets import SummernoteWidget


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = [
            'author',
            'slug',
            'updated_on',
            'created_on',
            'excerpt',
            ]

        labels = {
            'prep_time': 'Prep time (min)',
            'cook_time': 'Cook time (min)',
            'status': 'Save as Draft or Publish?',
            'is_public': 'Share it with the Community?',
        }
    
        # Summernote Widgets; customize toolbar
        # https://github.com/summernote/django-summernote
        widgets = {
            'ingredients': SummernoteWidget(attrs={'summernote': {'toolbar': [['para', ['ul']]]}}),
            'method': SummernoteWidget(attrs={'summernote': {'toolbar': [['para', ['ol']]]}})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {'body': Textarea(attrs={'rows': 2})}

        labels = {'body': ''}


