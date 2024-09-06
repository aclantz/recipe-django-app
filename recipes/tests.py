from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
  def setUpTestData():
    # set up non-modified objects for test methods
    Recipe.objects.create(name= "Tea", cooking_time= 3, ingredients= "Water, Tea Leaves, Honey", difficulty= "easy")
      
  def test_recipe_name(self):
    # get object to test
    recipe = Recipe.objects.get(id=1)
    # get metadata for name field
    field_label = recipe._meta.get_field('name').verbose_name
    # compare values
    self.assertEqual(field_label, 'name')

  def test_recipe_cooking_time(self):
    # get object to test
    recipe = Recipe.objects.get(id=1)
    # get metadata for name field
    field_label = recipe._meta.get_field('cooking_time').verbose_name
    # compare values
    self.assertEqual(field_label, 'cooking time')  # underscore taken away from 'cooking_time' because of .verbose_name

  def test_recipe_ingredients(self):
    # get object to test
    recipe = Recipe.objects.get(id=1)
    # get metadata for name field
    field_label = recipe._meta.get_field('ingredients').verbose_name
    # compare values
    self.assertEqual(field_label, 'ingredients')

  def test_recipe_difficulty(self):
    # get object to test
    recipe = Recipe.objects.get(id=1)
    # get metadata for name field
    field_label = recipe._meta.get_field('difficulty').verbose_name
    # compare values
    self.assertEqual(field_label, 'difficulty')

  def test_recipe_name_length(self):
    # get object to test
    recipe = Recipe.objects.get(id=1)
    # get metadata for the name field max_length
    max_length = recipe._meta.get_field('name').max_length
    # compare values
    self.assertEqual(max_length, 50)
      
  def test_recipe_ingredients_length(self):
    # get object to test
    recipe = Recipe.objects.get(id=1)
    # get metadata for the ingredients max_length    
    max_length = recipe._meta.get_field('ingredients').max_length
    # compare values
    self.assertEqual(max_length, 250)
      
    
