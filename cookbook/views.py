from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, is_public=True).order_by("-created_on")
    template_name = "browse_recipes.html"
    paginate_by = 6


class RecipeDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments
            }
        )
