# An Easy-To-Play, 2-Player Competitive Cooking Game

This is a 2-player competivie cooking game written using Python 3 for the final project of the course Programming for Business Computing.
The inspiration for the development of this game was the famous Nintendo Switch game *Overcooked*. Since I liked cooking for leisure, I thought it would be interesting to write an immitation of it. 

# Game Introduction

This game consists of 2 players. Let's call them P1 and P2 here. They compete to serve as many orders as possible within 60 seconds. When the game starts, on the top-left corner, there will be 2 randomly generated recipes. Players should move around the kitchen, pick up the correct ingredients and put them into the pot (there are 3 pots, either one can be used) in the correct order according to the recipes (wrong ingredients/order will result in inservable food). Once the food is ready to serve (as indicated by the text "done"), players should pick it up and put it in the serving area (area marked by the text "service please"). Once the food is served, a point will be added to the respective scoreboard of the player who's served the food and the recipe cooked will be replaced by another randomly generated recipe. 

A unique twist to this game is that players will be able to attack each other. If one player isn't holding any ingredient and the other is holding something, the former will be able to attack the latter and make him lose the ingredient he was holding, so he will have to go pick up the ingredient again. This increases the intensity of competition. :P

Once the time's up, the round is over. The scores of both players will be shown. You can choose to replay the game by clicking "Retry" at the end. 

# Key bindings for this game

Unfortunately, the 2 players must play this game on a single keyboard.

P1's movement is controlled by the 4 arrow keys on the keyboard and P2's W, A, S, D keys (corresponding to up, left, down, right). To pick up stuff, press V for P1 and left-click on the mouse for P2. To attack, press V for P1 and right-click on the mouse for P2.

|       | Player 1 | Player2     |
| :---        |    :----:   |          ---: |
| Movement     | Arrow Keys       | W, A, S, D   |
| Pick up/put down/drop ingredients/cooked food   | V         | Mouse left-click     |
| Attack | B | Mouse right-click|

# How to install and play this game on your computer?

Simply download the whole repository and run main.py using a Python 3 interpreter. You need the Python package pygame to play it, so if it hasn't been installed on your computer, you need to install it first. 


# Copyright disclaimer

The sound track was downloaded from https://www.youtube.com/watch?v=5APLVwcWgHk&t=98s. All images and graphs were hand-drawn. No copyright infringement is intended. 

