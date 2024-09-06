# default imports
from django.shortcuts import render, redirect
# my imports
from django.views.generic import ListView, DetailView         #to display lists
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin     #to protect CBV pages
from django.contrib.auth.decorators import login_required     #to protect FBV pages
import pandas as pd
from .forms import RecipeSearchForm, CreateRecipeForm         #form import
from .models import Recipe                                    #to access Recipe model

from .utils import get_chart


def home(request):                                            # base view for project
  return render(request, 'recipes/home.html')

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = 'recipes/list.html' 

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = 'recipes/details.html'

def about_view(request):
  return render(request, 'recipes/about.html')

@login_required
def SearchView(request):
  form = RecipeSearchForm(request.POST or None)
  recipes = Recipe.objects.all().values('name', 'cooking_time', 'difficulty', 'ingredients')      #GET all recipes
  recipe_df = None                                                                                #recipe_data-frame initialize
  chart = None                                                                                    #chart initialize
  qs = None

  if request.method == 'POST':
    # recipes = recipes.values('name', 'ingredients')
    recipe_title = request.POST.get('recipe_title')
    chart_type = request.POST.get('chart_type')
    print("*** POST: " + recipe_title, chart_type)                                                #terminal test
    qs = recipes.filter(name__icontains=recipe_title)
    print(f"*** QuerySet: {qs}")                                                                  #test to see query

    if qs.exists():
      recipe_df = pd.DataFrame(qs)                                                                #convert query-set values to pandas data-frame
      all_recipes_df = pd.DataFrame(recipes)
      chart = get_chart(chart_type, all_recipes_df, highlight_recipe=recipe_df.iloc[0])           #define chart params from data-frame values
      recipe_df = recipe_df[['name', 'ingredients']].to_html()                                    #convert data-frame to html

  context = {
    'form': form,
    'recipes': recipes,
    'recipe_df': recipe_df,
    'chart': chart,
    'qs': qs,
  }
  return render(request, 'recipes/search.html', context) 

@login_required
def CreateView(request):
  if request.method == 'POST':
        form = CreateRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.difficulty = new_recipe.calculate_difficulty()                     # Calculate difficulty
            new_recipe.save()                                                             # Save the new recipe to the database

            messages.success(request, "Your recipe has been successfully submitted!")
            form = CreateRecipeForm()
        else:
            messages.error(request, "There was an error with your submission.")
  else:
      form = CreateRecipeForm()
    
  context = {
      'form': form,
  }
  return render(request, 'recipes/create.html', context)
