from django import forms

CHART_CHOICES = (
  ('#1', 'Bar chart'),   
  ('#2', 'Pie chart'),
  ('#3', 'Line chart')
)

class RecipeSearchForm(forms.Form):
  recipe_title= forms.CharField(max_length=120)
  chart_type= forms.ChoiceField(choices=CHART_CHOICES)