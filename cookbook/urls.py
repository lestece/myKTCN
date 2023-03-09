from . import views
from django.urls import path

urlpatterns = [
    path('browse-recipes/', views.RecipeList.as_view(), name='browse-recipes'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
]