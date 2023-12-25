from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_chart, get_recipename_from_id
from django.db.models import Q

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


def home(request):
    return render(request, 'recipes/recipes_home.html')

def records(request):
    form = RecipesSearchForm(request.POST or None)
    recipe_df = None
    chart = None
    qs = None

    if form.is_valid():
        recipe_name = form.cleaned_data["recipe_name"]
        ingredients = form.cleaned_data["ingredients"]
        chart_type = form.cleaned_data["chart_type"]

        qs = Recipe.objects.all()

        if recipe_name:
            qs = qs.filter(Q(name__icontains=recipe_name))

        if ingredients:
            qs = qs.filter(Q(ingredients__icontains=ingredients))

        if not recipe_name and not ingredients:
            qs = Recipe.objects.all()

        if qs:
            recipe_df = pd.DataFrame(qs.values('id', 'name', 'cooking_time', 'ingredients'))
            chart = get_chart(chart_type, recipe_df, labels=recipe_df['name'].values)
            recipe_df = recipe_df.to_html()

    context = {
        'form': form,
        'recipe_df': recipe_df,
        'chart': chart,
        'qs': qs,
    }

    return render(request, 'recipes/search.html', context)