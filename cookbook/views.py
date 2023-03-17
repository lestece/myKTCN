from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.defaultfilters import slugify
from django.contrib import messages
from .models import Recipe, Rating
from .forms import RecipeForm, CommentForm


class Home(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newly_added_recipes'] = Recipe.objects.filter(status=1, is_public=True).order_by('-created_on')[:4]
        return context


class UserRecipes(generic.ListView):
    model = Recipe
    template_name = "cookbook.html"
    paginate_by = 8

    def get(self, request):
        queryset = Recipe.objects.filter(status=1, author=request.user.id).order_by("-created_on")
        queryset_dict = {'user_recipes': queryset}

        return render(
            request,
            self.template_name,
            queryset_dict,
        )
        

class UserDrafts(generic.ListView):
    model = Recipe
    template_name = "drafts.html"
    paginate_by = 12

    def get(self, request):
        queryset = Recipe.objects.filter(status=0, author=request.user.id).order_by("-created_on")
        queryset_dict = {'drafts': queryset}

        return render(
            request,
            self.template_name,
            queryset_dict,
        )


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1, is_public=True).order_by("-created_on")
    template_name = "browse_recipes.html"
    paginate_by = 8


class RecipeDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        # ratings = Rating.objects.filter(recipe=recipe.id)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        # rated = False
        # if ratings.user.filter(id=self.request.user.id).exists():
        #     rated = True
        rating = Rating.objects.filter(recipe=recipe, user=request.user).first()
        recipe.user_rating = rating.rating if rating else 0

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                # "rated": rated,
                "comment_form": CommentForm(),

            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        # ratings = Rating.objects.filter(recipe=recipe.id)
        comments = recipe.comments.filter(approved=True).order_by("created_on")
        # rated = False
        # if ratings.user.filter(id=self.request.user.id).exists():
        #     rated = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                # "rated": rated,
            },
        )


# API for Rating
# Rating system implemented thanks to this tutorial:
# https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c
def rate(request: HttpRequest, recipe_id: int, rating: int) -> HttpResponse:
    recipe = Recipe.objects.get(id=recipe_id)
    Rating.objects.filter(recipe=recipe, user=request.user).delete()
    recipe.rating_set.create(user=request.user, rating=rating)
    return rate(request)
# class RecipeRating(View):

#     def post(self, request, slug):
#         recipe = get_object_or_404(Recipe, slug=slug)
#         ratings = Rating.objects.filter(recipe=recipe.id)
#         if ratings.user.filter(id=self.request.user.id).exists():
#             ratings.user.remove(request.user)
#         else:
#             ratings.user.add(request.user)
#         return HttpResponseRedirect(reverse('recipe_details', args=[slug]))

# Generic editing views created following the documentation at:
# https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit
# and tutorials:
# https://www.youtube.com/watch?v=KB_wDXBwhUA
# https://www.youtube.com/watch?v=a718ii0Lf6M
# CRUD - C


class RecipeCreateView(CreateView):
    form_class = RecipeForm
    template_name = 'recipe_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)

    # Overwrite the absolute url reverse in the Recipe model 
    # Redirect differently based on recipe status (Published or draft)
    def get_success_url(self, **kwargs):
        if self.object.status == 0:
            return reverse_lazy('drafts')
        else:
            return reverse_lazy('recipe_details', kwargs={'slug': self.object.slug})


# CRUD - Update
class RecipeEditView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_edit.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


# CRUD - Delete
class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy('my_cookbook')

# class AddRecipe(View):
#     form_class = RecipeForm
#     template_name = 'add_recipe.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class
#         return render(
#             request,
#             self.template_name,
#             {
#                 "form": form,
#                 'posted': False,
#             }
#         )

#     def post(self, request, *args, **kwargs):
#         form = RecipeForm(data=request.POST)

#         if form.is_valid():
#             form.instance.author = request.user
#             form.instance.slug = slugify(form.instance.title)
#             title = form.instance.title
#             recipe = form.save(commit=False)
#             recipe.save()
#             return render(
#                 request,
#                 'add_recipe.html',
#                 {
#                     'posted': True,
#                     'title': title,
#                 }
#             )
#         else:
#             return render(
#                 request,
#                 'add_recipe.html',
#                 {
#                     'form': form,
#                     'failed': True,
#                     'posted': False,
#                 }
#             )
    

# class EditRecipe(UpdateView):
#     form_class = RecipeForm
#     template_name = 'edit_recipe.html'
#     success_url = '/thanks/'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         return super().form_valid(form)