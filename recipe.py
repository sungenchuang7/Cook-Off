import random
from constants import Ingredient

class recipeObj:
    def __init__(self, tomato_small, corn_small, tuna_small):
        self.recipe = []
        self.ingredient = [Ingredient.TOMATO, Ingredient.CORN, Ingredient.TUNA]
        self.tomato_small = tomato_small
        self.corn_small = corn_small
        self.tuna_small = tuna_small
        self.ingredient1 = tomato_small
        self.ingredient2 = corn_small
        self.ingredient3 = tuna_small

    def reset(self):
        self.recipe.clear()

    # if recipe is empty, generate a new one randomly
    def generateRecipe(self):
        if len(self.recipe) == 0:
            for i in range(3):  # 每份食譜由三樣食材或是三個份量的食材組合
                self.recipe.append(random.choice(self.ingredient))

            print('random recipe:', self.recipe)

            if self.recipe[0] == Ingredient.TOMATO:
                self.ingredient1 = self.tomato_small
            elif self.recipe[0] == Ingredient.CORN:
                self.ingredient1 = self.corn_small
            else:
                self.ingredient1 = self.tuna_small

            if self.recipe[1] == Ingredient.TOMATO:
                self.ingredient2 = self.tomato_small
            elif self.recipe[1] == Ingredient.CORN:
                self.ingredient2 = self.corn_small
            else:
                self.ingredient2 = self.tuna_small

            if self.recipe[2] == Ingredient.TOMATO:
                self.ingredient3 = self.tomato_small
            elif self.recipe[2] == Ingredient.CORN:
                self.ingredient3 = self.corn_small
            else:
                self.ingredient3 = self.tuna_small