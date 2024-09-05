# default imports
from django.shortcuts import render
# my imports
from django.views.generic import ListView, DetailView         #to display lists
from .models import Recipe                                    #to access Recipe model
from django.contrib.auth.mixins import LoginRequiredMixin     #to protect CBV pages
from django.contrib.auth.decorators import login_required     #to protect FBV pages
from .forms import RecipeSearchForm                           #form import
from .models import Recipe
import pandas as pd
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