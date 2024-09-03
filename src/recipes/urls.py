from django.urls import path
from .views import home, RecipeListView, RecipeDetailView, SearchView

app_name = 'recipes'

# map the URL to the view, each path() takes two params (route, view)
urlpatterns = [
  path('', home, name="home"),
  path('list/', RecipeListView.as_view(), name="list"),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
  path('search/', SearchView, name='search'),
]