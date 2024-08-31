# default imports
from django.db import models
# my imports
from django.shortcuts import reverse

# Create your models here.

class Recipe(models.Model):
  name= models.CharField(max_length=50)
  cooking_time= models.IntegerField()
  ingredients= models.TextField(max_length=250) 
  difficulty= models.CharField(max_length=12, default= None)
  directions = models.TextField(max_length=500, default= 'No directions added yet for this recipe')
  pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

  def __str__(self):
    return f"id: {self.id}, Name: {self.name}"

  def get_absolute_url(self):
      return reverse ('recipes:detail', kwargs={'pk': self.pk})
  
  def calculate_difficulty(self, cooking_time, ingredients):
     # calculate the difficulty based on two provided arguments
        if cooking_time < 10 and len(ingredients) < 4:
            difficulty = "Easy"
        elif cooking_time < 10 and len(ingredients) >= 4:
            difficulty = "Medium"
        elif cooking_time >= 10 and len(ingredients) < 4:
            difficulty = "Intermediate"
        elif cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = "Hard"
        return difficulty  