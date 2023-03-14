from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
from .forms import RecipeForm


class Home(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newly_added_recipes'] = Recipe.objects.filter(status=1, is_public=True).order_by('-created_on')[:4]
        return context


class UserRecipes(generic.ListView):
    model = Recipe
    template_name = "cookbook.html"
    paginate_by = 6

    def get(self, request):
        queryset = Recipe.objects.filter(status=1, author=request.user.id).order_by("-created_on")
        queryset_dict = {'user_recipes': queryset}

        return render(
            request,
            self.template_name,
            queryset_dict,
        )


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
        

class AddRecipe(View):
    form_class = RecipeForm
    template_name = 'add_recipe.html'

    def get(self, request):
        form = self.form_class
        return render(
            request,
            self.template_name,
            {
                "form": form,
            }
        )






    
