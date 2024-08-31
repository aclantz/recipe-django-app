from .views import Recipe

def test_get_absolute_url(self):
  recipe = Recipe.objects.get(id=1)
  #get_absolute_url() should take you to the detail page of book #1
  #and load the URL /books/list/1
  self.assertEqual(recipe.get_absolute_url(), '/recipe/list/1')

def test_ingredients_list(self):
  recipe = Recipe.objects.get(id=1)
  # test if string is returned as a list 
  self.assertEqual(recipe.ingredients_list(), ['Water', 'Coffee Grounds', 'Cream'])

def test_calculate_difficulty(self):
  recipe = Recipe.objects.get(id=1)
  # test if difficulty is returned
  self.assertEqual(recipe.calculate_difficulty(), 'Easy')