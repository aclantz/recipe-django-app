from django.urls import path
from .views import home

app_name = 'recipes'

# map the URL to the view, each path() takes two params (route, view)
urlpatterns = [
  path('', home),
]