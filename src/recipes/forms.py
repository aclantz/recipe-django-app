from django import forms
from .models import Recipe

CHART_CHOICES = (
  ('#1', 'Bar chart'),   
  ('#2', 'Pie chart'),
  ('#3', 'Line chart')
)

class RecipeSearchForm(forms.Form):
  recipe_title= forms.CharField(max_length=120)
  chart_type= forms.ChoiceField(choices=CHART_CHOICES)

class CreateRecipeForm(forms.ModelForm):
  class Meta:
    model = Recipe
    fields = ['name', 'cooking_time', 'ingredients', 'directions', 'pic']  # Include the image field
