from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# from my project
from .models import Recipe
from .forms import RecipeSearchForm
from .views import SearchView

class test_recipe_search_form(TestCase):
  def test_recipe_title_field_label(self):
    form = RecipeSearchForm()
    self.assertTrue(form.fields['recipe_title'].label is None or form.fields['recipe_title'].label == 'Recipe title')

  def test_recipe_title_max_length(self):
    form = RecipeSearchForm()
    self.assertEqual(form.fields['recipe_title'].max_length, 120)

  def test_chart_type_choices(self):
    form = RecipeSearchForm()
    expected_choices = [('#1', 'Bar chart'), ('#2', 'Pie chart'), ('#3', 'Line chart')]
    self.assertEqual(form.fields['chart_type'].choices, expected_choices)


class TestSearchView(TestCase):
  def setUp(self):
      self.client = Client()
      self.user = User.objects.create_user(username='testuser', password='testpassword')
      self.client.login(username='testuser', password='testpassword')
      # Create sample recipes
      self.recipe1 = Recipe.objects.create(name="Spaghetti", cooking_time=30, difficulty="Easy", ingredients="Pasta, Tomato")
      self.recipe2 = Recipe.objects.create(name="Pancakes", cooking_time=15, difficulty="Medium", ingredients="Flour, Eggs, Milk")
      self.url = reverse('recipes:search')  

  def test_search_view_post(self):
      data = {'recipe_title': 'Spaghetti', 'chart_type': '#1'}
      response = self.client.post(self.url, data)
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, 'Spaghetti')
      self.assertIn('chart', response.context)

  def test_search_view_no_results(self):
      data = {'recipe_title': 'Nonexistent Recipe', 'chart_type': '#1'}
      response = self.client.post(self.url, data)
      self.assertEqual(response.status_code, 200)
      self.assertIsNone(response.context['recipe_df'])
      self.assertNotIn('Nonexistent Recipe', response.context.get('qs', []))  # Ensure the queryset is empty

  def test_search_view_no_post(self):
      response = self.client.get(self.url)
      self.assertEqual(response.status_code, 200)
      self.assertIn('form', response.context)
      self.assertIn('recipes', response.context)
      self.assertIsNone(response.context['recipe_df'])

  def test_search_view_login_required(self):
      self.client.logout()
      response = self.client.get(self.url)
      self.assertNotEqual(response.status_code, 200)
      self.assertRedirects(response, '/login/' + f'?next={self.url}')  