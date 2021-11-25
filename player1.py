import pygame
from images_path import ImagePath1
from constants import Config, Ingredient, Dish, Act

pygame.init()
screen = pygame.display.set_mode(Config.APP_SIZE)

imgSize = [[104, 48], [103, 87], [103, 87], [103, 87], [103, 105], [104, 106], [105, 80]]  # direction = N


class Chef:
    img_man = [
        pygame.image.load(ImagePath1.MAN_NORTH).convert_alpha(),
        pygame.image.load(ImagePath1.MAN_SOUTH).convert_alpha(),
        pygame.image.load(ImagePath1.MAN_WEST).convert_alpha(),
        pygame.image.load(ImagePath1.MAN_EAST).convert_alpha()
    ]  # N.S.W.E

    img_manWithFish = [
        pygame.image.load(ImagePath1.TUNA_NORTH).convert_alpha(),
        pygame.image.load(ImagePath1.TUNA_SOUTH).convert_alpha(),
        pygame.image.load(ImagePath1.TUNA_WEST).convert_alpha(),
        pygame.image.load(ImagePath1.TUNA_EAST).convert_alpha()
    ]

    img_manWithCorn = [
        pygame.image.load(ImagePath1.CORN_NORTH).convert_alpha(),
        pygame.image.load(ImagePath1.CORN_SOUTH).convert_alpha(),
        pygame.image.load(ImagePath1.CORN_WEST).convert_alpha(),
        pygame.image.load(ImagePath1.CORN_EAST).convert_alpha()
    ]

    img_manWithToma = [
        pygame.image.load(ImagePath1.TOMATO_NORTH).convert_alpha(),
        pygame.image.load(ImagePath1.TOMATO_SOUTH).convert_alpha(),
        pygame.image.load(ImagePath1.TOMATO_WEST).convert_alpha(),
        pygame.image.load(ImagePath1.TOMATO_EAST).convert_alpha()
    ]

    img_good = [
        pygame.image.load(ImagePath1.GOOD_NORTH).convert_alpha(),
        pygame.image.load(ImagePath1.GOOD_SOUTH).convert_alpha(),
        pygame.image.load(ImagePath1.GOOD_WEST).convert_alpha(),
        pygame.image.load(ImagePath1.GOOD_EAST).convert_alpha()
    ]

    img_bad = [
        pygame.image.load(ImagePath1.BAD_NORTH).convert_alpha(),
        pygame.image.load(ImagePath1.BAD_SOUTH).convert_alpha(),
        pygame.image.load(ImagePath1.BAD_WEST).convert_alpha(),
        pygame.image.load(ImagePath1.BAD_EAST).convert_alpha()
    ]

    img_hit = [
        pygame.image.load(ImagePath1.HIT_NORTH).convert_alpha(),
        pygame.image.load(ImagePath1.HIT_SOUTH).convert_alpha(),
        pygame.image.load(ImagePath1.HIT_WEST).convert_alpha(),
        pygame.image.load(ImagePath1.HIT_EAST).convert_alpha()
    ]

    # pygame.image.load(ImagePath1.MEMO).convert_alpha()

    find = {
        Ingredient.EMPTY: 0,
        Ingredient.TUNA: 1,
        Ingredient.TOMATO: 2,
        Ingredient.CORN: 3,
        Dish.GOOD: 4,
        Dish.BAD: 5,
        Act.HIT: 6
    }  # dictionary

    imgList = [img_man, img_manWithFish, img_manWithToma, img_manWithCorn, img_good, img_bad, img_hit]

    def __init__(self, manX, manY, d, w, h, food):
        self.x = manX
        self.y = manY
        self.direction = d  # N, S, W, E
        self.width = w
        self.height = h
        self.take = food  # "0", "tuna", "tomato", "corn", "good", "bad", "hit"
        self.rect = self.imgList[self.find[self.take]][self.direction].get_rect()
        self.rect.center = (self.x, self.y)

    def BumpAtFirst(self):  # revise x & y due to w & h switch or image change
        if (self.x < 100 and 90 - self.height < self.y):  # tomato table
            self.y = 90 - self.height
        elif (100 > self.y and self.x + self.width > 519):  # corn table
            self.x = 519 - self.width
        elif (500 < self.y + self.height and self.x + self.width > 300):  # fish table
            if self.x > 300:
                self.y = 500 - self.height
            else:
                self.x = 300 - self.width

    # stuck in tuna table
    def BumpIntoTable(self):
        if ((self.x < 100 and 90 - self.height < self.y) or
                (100 > self.y and self.x + self.width > 519) or
                (500 < self.y + self.height and self.x + self.width > 300)):
            return 1
        return 0

    def TurnTo(self, n):
        if (((self.direction == 0 or self.direction == 1) and (n == 2 or n == 3)) or
                ((self.direction == 2 or self.direction == 3) and (n == 0 or n == 1))):
            # revise width & height when turn to different directions
            temp = self.width
            self.width = self.height
            self.height = temp

            self.BumpAtFirst()
        self.direction = n

    def useImage(self):
        takeObject = self.find[self.take]   # id
        pdf = self.imgList[takeObject][self.direction]
        
        # w & h are controled by: object taken by chef and chef's direction 
        if self.direction == 2 or self.direction == 3:
            self.width = imgSize[takeObject][1]
            self.height = imgSize[takeObject][0]
        else:
            self.width = imgSize[takeObject][0]
            self.height = imgSize[takeObject][1]
        return pdf

    def Move(self):  # revise x & y
        worldx = 1000
        worldy = 600
        vel = 2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > vel:
            self.TurnTo(2)  # W
            self.x -= vel
            if (self.BumpIntoTable()):
                self.x += vel
        if keys[pygame.K_RIGHT] and self.x < worldx - self.width - vel:
            self.TurnTo(3)  # E
            self.x += vel
            if (self.BumpIntoTable()):
                self.x -= vel
        if keys[pygame.K_UP] and self.y > vel:
            self.TurnTo(0)  # N
            self.y -= vel
            if (self.BumpIntoTable()):
                self.y += vel
        if keys[pygame.K_DOWN] and self.y < worldy - self.height - vel:
            self.TurnTo(1)  # S
            self.y += vel
            if (self.BumpIntoTable()):
                self.y -= vel

        self.rect.center = (self.x + self.width / 2, self.y + self.height / 2)  # parameter need correct

    def ifClick(self):
        press = pygame.mouse.get_pressed()
        if press[0]:
            return True
        else:
            return False

    def ifAttack(self):
        press = pygame.mouse.get_pressed()
        if press[2]:
            return True
        else:
            return False

    def setFood(self, takeType):
        self.take = takeType
        if takeType == Dish.BAD:
            pygame.mixer.Sound('./sound/wtf.mp3').play(0)

