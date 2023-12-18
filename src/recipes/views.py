from django.shortcuts import render
from django.views.generic import ListView, DetailView     # to display list of objects and details of a single object
from django.contrib.auth.mixins import LoginRequiredMixin # to restrict access to views
from .models import Recipe                                # to access the Recipe model

# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):       # class-based 'protected' view
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):   # class-based 'protected' view
    model = Recipe
    template_name = 'recipes/detail.html'


def home(request):
    return render(request, 'recipes/recipes_home.html')