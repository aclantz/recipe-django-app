# default imports
from django.shortcuts import render
# my imports
from django.views.generic import ListView, DetailView         #to display lists
from .models import Recipe                                    #to access Recipe model
from django.contrib.auth.mixins import LoginRequiredMixin     #to protect CBV pages
from .forms import RecipeSearchForm                           #form import
from .models import Recipe
import pandas as pd
from .utils import get_chart

# Create your views here.
# base view for project
def home(request):
  return render(request, 'recipes/home.html')

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = 'recipes/list.html' 

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = 'recipes/details.html'

def SearchView(request):
  form = RecipeSearchForm(request.POST or None)
  recipes = Recipe.objects.all()                              #GET all recipes
  recipe_df = None                                            #recipe_data-frame initialize
  chart = None                                                #chart initialize
  qs = None

  if request.method == 'POST':
    if 'view_all' in request.POST:
      qs = recipes.values('name', 'ingredients')
      chart_type = None
    else:
      recipe_title = request.POST.get('recipe_title')
      chart_type = request.POST.get('chart_type')
      print(recipe_title, chart_type)                                                #terminal test
      qs = Recipe.objects.filter(name__icontains=recipe_title)\
        .values('name', 'ingredients', 'cooking_time', 'difficulty')                 #apply filter to extract data
      print(f"QuerySet: {qs}")                                                       #test to see query

    if qs.exists():
      recipe_df = pd.DataFrame(qs)                                                 #convert query-set values to pandas data-frame
      chart = get_chart(chart_type, recipe_df, labels=recipe_df['name'].values)     #define chart params from data-frame values
      recipe_df = recipe_df[['name', 'ingredients']].to_html()                                                       #convert data-frame to html


  context = {
    'form': form,
    'recipes': recipes,
    'recipe_df': recipe_df,
    'chart': chart,
    'qs': qs,
  }
  return render(request, 'recipes/search.html', context) 