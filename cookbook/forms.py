# Forms for the adding/editing a recipe and commenting a recipe

from django import forms
from django.forms import ModelForm, Textarea
from .models import Recipe, Comment
from django_summernote.widgets import SummernoteWidget


class RecipeForm(forms.ModelForm):
    # Get the Recipe model
    class Meta:
        model = Recipe
        fields = '__all__'
        # Exclude the unnecessary field from the form
        exclude = [
            'author',
            'slug',
            'updated_on',
            'created_on',
            'excerpt',
            ]
        # Change the form fields label
        labels = {
            'prep_time': 'Prep time (min)',
            'cook_time': 'Cook time (min)',
            'status': 'Save as Draft or Publish?',
            'is_public': 'Share it with the Community?',
        }
    
        '''
        Add Summernote Widgets to ingredients and method fields; customize toolbar.
        https://github.com/summernote/django-summernote '''
        widgets = {
            'ingredients': SummernoteWidget(attrs={'summernote': {'toolbar': [['para', ['ul']]]}}),
            'method': SummernoteWidget(attrs={'summernote': {'toolbar': [['para', ['ol']]]}})
        }


class CommentForm(forms.ModelForm):
    # Get the Comment model and display only the body field to the user
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {'body': Textarea(attrs={'rows': 2})}

        labels = {'body': ''}


