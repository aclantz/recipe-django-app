from django.shortcuts import render

# Create your views here.
# base view for project
def home(request):
  return render(request, 'recipes/home.html')

