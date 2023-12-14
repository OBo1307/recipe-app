from django.shortcuts import render
from django.views.generic import ListView, DetailView # to display list of objects and details of a single object
from .models import Recipe # to access the Recipe model

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


def home(request):
    return render(request, 'recipes/recipes_home.html')