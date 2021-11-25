import pygame
import math
import sys
import os
from pygame.locals import *
from images_path import ImagePath1
from constants import Ingredient, Dish, Config, Act
from pot import Pot
from recipe import recipeObj
from timer import timer
from player1 import Chef
from player2 import Chef2

pygame.init()
pygame.mixer.init()


pygame.mixer.Sound('./sound/Overcooked2Soundtrack.mp3').play(0)
# pygame.mixer.music.play(0)


vel = 2
screen = pygame.display.set_mode(Config.APP_SIZE)
pygame.display.set_caption(Config.APP_NAME)

background = pygame.image.load(ImagePath1.BACKGROUND).convert()
img_pot = pygame.image.load(ImagePath1.POT).convert_alpha()
img_pot_with_ingredient = pygame.image.load(ImagePath1.POT_WITH_INGREDIENT).convert_alpha()
img_potCooking = pygame.image.load(ImagePath1.POT_COOKING).convert_alpha()

imgSize = [[104, 48], [103, 87], [103, 87], [103, 87], [103, 105], [104, 106], [105, 80]]  # direction = N
#########################################################################
corn = pygame.Surface((10, 140))
corn.fill((150, 150, 150))
cornSitu = corn.get_rect()
cornSitu.center = (720, 55)

tuna = pygame.Surface((10, 110))
tuna.fill((150, 150, 150))
tunaSitu = tuna.get_rect()
tunaSitu.center = (865, 480)

toma = pygame.Surface((120, 20))
toma.fill((150, 150, 150))
tomaSitu = toma.get_rect()
tomaSitu.center = (80, 510)

scorePoint = pygame.Surface((10, 100))
scorePoint.fill((150, 150, 150))
scorePointSitu = scorePoint.get_rect()
scorePointSitu.center = (430, 500)

# FIXME: pot1 check boundary optimization
pot_1 = pygame.Surface((100, 100))
pot_1.fill((150, 150, 150))
pot_1_Situ = pot_1.get_rect()
pot_1_Situ.center = (72, 300)

# FIXME: pot2 heck boundary optimization
pot_2 = pygame.Surface((100, 100))
pot_2.fill((150, 150, 150))
pot_2_Situ = pot_2.get_rect()
pot_2_Situ.center = (600, 500)

# FIXME: pot3 heck boundary optimization
pot_3 = pygame.Surface((100, 100))
pot_3.fill((150, 150, 150))
pot_3_Situ = pot_3.get_rect()
pot_3_Situ.center = (72, 220)


########################################
# callback from pot
def serve_dish(dish, playerNum):
    """ callback - pot serve dish to chef  """
    if playerNum == 1:
        player1.setFood(dish)
    elif playerNum == 2:
        player2.setFood(dish)

########################################
# two players' score
totalScore1 = totalScore2 = 0
scoreFont = pygame.font.SysFont("Arial", 23)
scoreText = scoreFont.render("Score: " + str(int(totalScore1)).zfill(2), True, (255, 255, 255))
finalScreen = pygame.font.SysFont("Arial", 30)
finalScreen = pygame.Surface(Config.APP_SIZE)
finalScreen.fill((255, 255, 255))
########################################

player1 = Chef(475, 275, 0, imgSize[0][0], imgSize[0][1], Ingredient.EMPTY)
player2 = Chef2(150, 275, 0, imgSize[0][0], imgSize[0][1], Ingredient.EMPTY)
screen.blit(player1.img_man[0], (player1.x, player1.y))
screen.blit(player2.img_man[0], (player2.x, player2.y))

recipe1 = recipeObj(pygame.image.load(ImagePath1.TOMATO_SMALL).convert_alpha(),
                   pygame.image.load(ImagePath1.CORN_SMALL).convert_alpha(),
                   pygame.image.load(ImagePath1.TUNA_SMALL).convert_alpha())
recipe2 = recipeObj(pygame.image.load(ImagePath1.TOMATO_SMALL).convert_alpha(),
                   pygame.image.load(ImagePath1.CORN_SMALL).convert_alpha(),
                   pygame.image.load(ImagePath1.TUNA_SMALL).convert_alpha())

timer = timer()

run = []
run.append(1)

left_pot = Pot(Config.LEFT_POT_NAME, 5, 280, serve_dish)
right_pot = Pot(Config.RIGHT_POT_NAME, 600, 500, serve_dish)
up_pot = Pot(Config.UP_POT_NAME, 5, 140, serve_dish)

running = True
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

while running:
    pygame.time.delay(2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player1.Move()
    player2.Move()
    pdf1 = player1.useImage()
    pdf2 = player2.useImage()


    # show players
    screen.blit(background, (0, 0))
    screen.blit(pdf1, (player1.x, player1.y))
    screen.blit(pdf2, (player2.x, player2.y))
    recipe1.generateRecipe()
    recipe2.generateRecipe()
    left_pot.set_recipe(recipe1.recipe, recipe2.recipe)
    right_pot.set_recipe(recipe1.recipe, recipe2.recipe)
    up_pot.set_recipe(recipe1.recipe, recipe2.recipe)


    # show recipe
    screen.blit(pygame.image.load(ImagePath1.MEMO), (11, 10))
    screen.blit(pygame.image.load(ImagePath1.MEMO), (122, 10))
    screen.blit(recipe1.ingredient1, (20, 15))
    screen.blit(recipe1.ingredient2, (60, 15))
    screen.blit(recipe1.ingredient3, (20, 50))
    screen.blit(recipe2.ingredient1, (130, 15))
    screen.blit(recipe2.ingredient2, (170, 15))
    screen.blit(recipe2.ingredient3, (130, 50))

    if left_pot.is_cooking:
        left_pot.checkCooking()
    if right_pot.is_cooking:
        right_pot.checkCooking()
    if up_pot.is_cooking:
        up_pot.checkCooking()


    # render pots
    if left_pot.is_cooking or not left_pot.is_good is None:
        screen.blit(img_potCooking, (left_pot.x, left_pot.y))
    elif not left_pot.is_cooking and left_pot.get_ingredient_count() > 0:
        screen.blit(img_pot_with_ingredient, (left_pot.x, left_pot.y))
    else:
        screen.blit(img_pot, (left_pot.x, left_pot.y))

    if right_pot.is_cooking or not right_pot.is_good is None:
        screen.blit(img_potCooking, (right_pot.x, right_pot.y))
    elif not right_pot.is_cooking and right_pot.get_ingredient_count() > 0:
        screen.blit(img_pot_with_ingredient, (right_pot.x, right_pot.y))
    else:
        screen.blit(img_pot, (right_pot.x, right_pot.y))

    if up_pot.is_cooking or not up_pot.is_good is None:
        screen.blit(img_potCooking, (up_pot.x, up_pot.y))
    elif not up_pot.is_cooking and up_pot.get_ingredient_count() > 0:
        screen.blit(img_pot_with_ingredient, (up_pot.x, up_pot.y))
    else:
        screen.blit(img_pot, (up_pot.x, up_pot.y))


    # check pot render text
    if not left_pot.render_text is None:
        font = pygame.font.SysFont('Arial', 20)
        screen.blit(font.render(left_pot.render_text, True, (255, 0, 0)), Config.LEFT_COOKING_TEXT_COORDINATE)

    if not right_pot.render_text is None:
        font = pygame.font.SysFont('Arial', 20)
        screen.blit(font.render(right_pot.render_text, True, (255, 0, 0)), Config.RIGHT_COOKING_TEXT_COORDINATE)

    if not up_pot.render_text is None:
        font = pygame.font.SysFont('Arial', 20)
        screen.blit(font.render(up_pot.render_text, True, (255, 0, 0)), Config.UP_COOKING_TEXT_COORDINATE)


    # player1 press event
    if player1.ifAttack() and player1.take == Ingredient.EMPTY:
        player1.setFood(Act.HIT)
        pygame.mixer.Sound('./sound/swing.mp3').play(0)
    elif player1.take == Act.HIT:
        player1.setFood(Ingredient.EMPTY)

    if pygame.Rect.colliderect(player1.rect, cornSitu) and player1.ifClick():
        player1.setFood(Ingredient.CORN)
        pygame.mixer.Sound('./sound/grab.mp3').play(0)
    elif pygame.Rect.colliderect(player1.rect, tunaSitu) and player1.ifClick():
        player1.setFood(Ingredient.TUNA)
        pygame.mixer.Sound('./sound/grab.mp3').play(0)
    elif pygame.Rect.colliderect(player1.rect, tomaSitu) and player1.ifClick():
        player1.setFood(Ingredient.TOMATO)
        pygame.mixer.Sound('./sound/grab.mp3').play(0)
    elif pygame.Rect.colliderect(player1.rect, pot_1_Situ) and player1.ifClick():
        left_pot.add_ingredient(player1.take, 1)
    elif pygame.Rect.colliderect(player1.rect, pot_2_Situ) and player1.ifClick():
        right_pot.add_ingredient(player1.take, 1)
    elif pygame.Rect.colliderect(player1.rect, pot_3_Situ) and player1.ifClick():
        up_pot.add_ingredient(player1.take, 1)
    elif pygame.Rect.colliderect(player1.rect, scorePointSitu) and player1.ifClick():
        if player1.take == 'good':
            pygame.mixer.Sound('./sound/correct.mp3').play(0)
            totalScore1 += 1
        player1.setFood(Ingredient.EMPTY)
    elif player1.ifClick() and (player1.take != Ingredient.EMPTY and player1.take != Act.HIT):
        player1.setFood(Ingredient.EMPTY)


    # player2 press event
    if player2.ifAttack() and player2.take == Ingredient.EMPTY:
        player2.setFood(Act.HIT)
        pygame.mixer.Sound('./sound/swing.mp3').play(0)
    elif player2.take == Act.HIT:
        player2.setFood(Ingredient.EMPTY)

    if pygame.Rect.colliderect(player2.rect, cornSitu) and player2.ifClick():
        player2.setFood(Ingredient.CORN)
        pygame.mixer.Sound('./sound/grab.mp3').play(0)
    elif pygame.Rect.colliderect(player2.rect, tunaSitu) and player2.ifClick():
        player2.setFood(Ingredient.TUNA)
        pygame.mixer.Sound('./sound/grab.mp3').play(0)
    elif pygame.Rect.colliderect(player2.rect, tomaSitu) and player2.ifClick():
        player2.setFood(Ingredient.TOMATO)
        pygame.mixer.Sound('./sound/grab.mp3').play(0)
    elif pygame.Rect.colliderect(player2.rect, pot_1_Situ) and player2.ifClick():
        left_pot.add_ingredient(player2.take, 2)
    elif pygame.Rect.colliderect(player2.rect, pot_2_Situ) and player2.ifClick():
        right_pot.add_ingredient(player2.take, 2)
    elif pygame.Rect.colliderect(player2.rect, pot_3_Situ) and player2.ifClick():
        up_pot.add_ingredient(player2.take, 2)
    elif pygame.Rect.colliderect(player2.rect, scorePointSitu) and player2.ifClick():
        if player2.take == 'good':
            totalScore2 += 1
            pygame.mixer.Sound('./sound/correct.mp3').play(0)
        player2.setFood(Ingredient.EMPTY)
    elif player2.ifClick() and (player2.take != Ingredient.EMPTY and player2.take != Act.HIT):
        player2.setFood(Ingredient.EMPTY)


    # hit and drop
    if abs(player1.x - player2.x) + abs(player1.y - player2.y) <= 50:
        if player1.take == Act.HIT:
            player2.setFood(Ingredient.EMPTY)
            pygame.mixer.Sound('./sound/hit.mp3').play(0)
        if player2.take == Act.HIT:
            player1.setFood(Ingredient.EMPTY)
            pygame.mixer.Sound('./sound/hit.mp3').play(0)


    # show current time, score
    timer.startCount(run)
    screen.blit(timer.text, (810, 10))
    scoreText1 = scoreFont.render("player1: " + str(int(totalScore1)), True, (255, 255, 255))
    screen.blit(scoreText1, (790, 60)) # adjust situation
    scoreText2 = scoreFont.render("player2: " + str(int(totalScore2)), True, (255, 255, 255))
    screen.blit(scoreText2, (900, 60)) # adjust situation


    # when game end
    if run[0] == 0:
        screen.blit(finalScreen, (0,0))
        screen.blit(pygame.image.load(ImagePath1.TUNA), (320, 250))
        finalText1 = scoreFont.render("player1: " + str(int(totalScore1)).zfill(2), True, (0, 0, 0))
        screen.blit(finalText1, (350, 225))
        finalText2 = scoreFont.render("player2: " + str(int(totalScore2)).zfill(2), True, (0, 0, 0))
        screen.blit(finalText2, (350, 325))
        screen.blit(pygame.image.load(ImagePath1.TUNA), (540, 250))
        finalText = scoreFont.render("Retry", True, (0, 0, 0))
        screen.blit(finalText, (580, 320))
        
        press = pygame.mouse.get_pressed()
        if press[0] and (550 < pygame.mouse.get_pos()[0] < 700 and 260 < pygame.mouse.get_pos()[1] < 350):
            run[0] = 1
            timer.setStart(60)
            totalScore1 = 0
            totalScore2 = 0
            left_pot = Pot(Config.LEFT_POT_NAME, 5, 280, serve_dish)
            right_pot = Pot(Config.RIGHT_POT_NAME, 600, 500, serve_dish)
            up_pot = Pot(Config.UP_POT_NAME, 5, 140, serve_dish)
            player1 = Chef(475, 275, 0, imgSize[0][0], imgSize[0][1], Ingredient.EMPTY)
            player2 = Chef2(150, 275, 0, imgSize[0][0], imgSize[0][1], Ingredient.EMPTY)
            recipe1.reset()
            recipe2.reset()

    #####################################################################
    # pygame.display.update()
    pygame.display.flip()

pygame.quit()
