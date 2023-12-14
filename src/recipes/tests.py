from django.test import TestCase
from .models import Recipe
# Create your tests here.

class RecipeModelTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(
            name='Test Recipe',
            cooking_time=15,
            ingredients='Ingredient 1, Ingredient 2, Ingredient 3',
            description='Test recipe description'
        )

    def test_recipe_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')

    def test_calculate_difficulty_easy(self):
        recipe = Recipe.objects.get(id=1)
        recipe.cooking_time = 5
        recipe.ingredients = 'Ingredient 1, Ingredient 2'
        expected_difficulty = 'Easy'
        self.assertEqual(recipe.calculate_difficulty(), expected_difficulty)
    
    def test_calculate_difficulty_medium(self):
        recipe = Recipe.objects.get(id=1)
        recipe.cooking_time = 5
        recipe.ingredients = 'Ingredient 1, Ingredient 2, Ingredient 3, Ingredient 4, Ingredient 5, Ingredient 6, Ingredient 7'
        expected_difficulty = 'Medium'
        self.assertEqual(recipe.calculate_difficulty(), expected_difficulty)

    def test_calculate_difficulty_intermediate(self):
        recipe = Recipe.objects.get(id=1)
        recipe.cooking_time = 15
        recipe.ingredients = 'Ingredient 1, Ingredient 2'
        expected_difficulty = 'Intermediate'
        self.assertEqual(recipe.calculate_difficulty(), expected_difficulty)

    def test_calculate_difficulty_hard(self):
        recipe = Recipe.objects.get(id=1)
        recipe.cooking_time = 15
        recipe.ingredients = 'Ingredient 1, Ingredient 2, Ingredient 3, Ingredient 4, Ingredient 5, Ingredient 6, Ingredient 7'
        expected_difficulty = 'Hard'
        self.assertEqual(recipe.calculate_difficulty(), expected_difficulty)
