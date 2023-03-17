from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('browserecipes/', views.RecipeList.as_view(), name='browse_recipes'),
    path('my_cookbook/', views.UserRecipes.as_view(), name='my_cookbook'),
    path('create/', views.RecipeCreateView.as_view(), name='create_recipe'),
    path('my_drafts/', views.UserDrafts.as_view(), name='drafts'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
    path('<slug:slug>/update/', views.RecipeEditView.as_view(), name='edit_recipe'),
    path('<slug:slug>/delete/', views.RecipeDeleteView.as_view(), name='delete_recipe'),
    path('rate/<int:recipe_id>/<int:rating>/', views.rate),
]