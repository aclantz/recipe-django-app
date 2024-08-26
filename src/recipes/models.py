from django.db import models

# Create your models here.
class Recipe(models.Model):
  name= models.CharField(max_length=50)
  cooking_time= models.IntegerField()
  ingredients= models.TextField(max_length=250) 
  difficulty= models.CharField(max_length=12, default= None)

  def __str__(self):
    return f"id: {self.id}, Name: {self.name}"