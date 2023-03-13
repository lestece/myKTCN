from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('browserecipes/', views.RecipeList.as_view(), name='browse_recipes'),
    path('my_cookbook/', views.UserRecipes.as_view(), name='my_cookbook'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
]