# default imports
from django.shortcuts import render
# my imports
from django.views.generic import ListView, DetailView   #to display lists
from .models import Recipe                  #to access Recipe model

# Create your views here.
# base view for project
def home(request):
  return render(request, 'recipes/home.html')

class RecipeListView(ListView):
  model = Recipe
  template_name = 'recipes/list.html' #maybe need to rename that ***

class RecipeDetailView(DetailView):
  model = Recipe
  template_name = 'recipes/details.html'