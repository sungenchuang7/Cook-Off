import time
import pygame
from constants import Ingredient, Dish, Config


class Pot:
    def __init__(self, name, x, y, serve_dish_callback):
        self.name = name
        self.inside = []
        self.recipe1 = []
        self.recipe2 = []
        self.serve_dish = serve_dish_callback
        self.is_good = None
        self.is_cooking = False
        self.render_text = None
        self.x = x
        self.y = y
        self.mappingRecipe = 0
        self.startTime = 0
        self.nowTime = 0

    def _reset_pot(self):
        """ private function - reset pot to init state """
        self.is_good = None
        self.is_cooking = False
        self.render_text = None
        self.inside.clear()
        self.startTime = 0
        self.nowTime = 0
        if self.mappingRecipe == 1:
            self.recipe1.clear()
        elif self.mappingRecipe == 2:
            self.recipe2.clear()

    def set_recipe(self, recipe1, recipe2):
        """ set current recipe for compare good or bad """
        self.recipe1 = recipe1
        self.recipe2 = recipe2

    def add_ingredient(self, ingredient, playerNum):
        """ add ingredient in to pot """

        if (ingredient == Ingredient.CORN or ingredient == Ingredient.TOMATO or ingredient == Ingredient.TUNA) and len(
                self.inside) < 3:
            # can put ingredient in pot
            pygame.mixer.Sound('./sound/putIngredient.mp3').play(0)
            self.inside.append(ingredient)
            self.serve_dish(Ingredient.EMPTY, playerNum)

            self._check_is_ready_to_cook()
        elif ingredient == Ingredient.EMPTY:
            # if chef is empty hand
            if not self.is_good is None:
                # if dish is ready
                if self.is_good:
                    self.serve_dish(Dish.GOOD, playerNum)
                else:
                    self.serve_dish(Dish.BAD, playerNum)

                # reset pot to init
                self._reset_pot()

    def get_ingredient_count(self) -> int:
        """ get current pot ingredient count """
        return len(self.inside)

    def _check_is_ready_to_cook(self):
        """ check is pot ready to cook """
        if not self.is_cooking and self.is_good is None and len(self.inside) >= 3:
            self._start_cooking()

    def _start_cooking(self):
        """ start to cook """
        self.is_cooking = True
        self.render_text = Config.COOKING_TEXT
        pygame.mixer.Sound('./sound/boiling.mp3').play(0)
        # start a new thread to count down
        self.startTime = time.time()

    def checkCooking(self):
        self.nowTime = time.time()
        """ private function - open a new thread to count down """
        if self.nowTime - self.startTime > Config.COOKING_TIME:
            # done of cooking
            self.is_cooking = False
            self.render_text = Config.COOKED_DONE_TEXT

            current_recipe1 = self.recipe1
            current_recipe2 = self.recipe2
            # -----------------------------------

            print('-----------------------')
            print('current recipe1:', current_recipe1, 'current recipe2:', current_recipe2, ', inside:', self.inside)
            print('-----------------------')

            if current_recipe1 == self.inside:
                self.is_good = True
                self.mappingRecipe = 1
            elif current_recipe2 == self.inside:
                self.is_good = True
                self.mappingRecipe = 2
            else:
                self.is_good = False
                self.mappingRecipe = 0

            print('cooking result:', self.is_good)
