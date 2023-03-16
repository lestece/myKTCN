from django import forms
from django.forms import ModelForm, Textarea
from .models import Recipe, Comment


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
            'status': 'Save as Draft or Publish?',
            'is_public': 'Share it with the Community?',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {'body': Textarea(attrs={'rows': 2})}

        labels = {'body': ''}
