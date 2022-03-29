"""
The main file takes the GameBoard, GameBrain, Write, and WaitTurtle classes and creates a memory game with python.
------------------------------------------------------------------------------------------------------------------------

NOTE: Where appropriate I commented with hashtags #, on top of a block of code to explain what it does,
where an explanation of the code in a function was not needed I only wrote a docstring at the top explaining what
the function does.

NOTE: Words that have a definition will be written with an asterisk on either sides of them.
For example: runs through the turtles contained in the *game board* and hides them

------------------------------------------------------------------------------------------------------------------------

Definitions:

Turtle object - An instance of the class Turtle from the turtle module.
Essentially a little turtle you can move around and paint with, in my case I change their shape to squares.

game board - A list of 8 lists, each of those containing 8 Turtle objects.
Each of these turtles is a white square and arranged in an 8 by 8 grid.

random board - A board (in this case an edited version of the game board) where for each row,
there is one Turtle colored light blue (this is the turtle I want the user to memorize)

mask board - A new board that covers the main game board, it is a mask that will either hide or show the
random board that lies behind it by hiding or showing the Turtles that are in the mask board.

square number - A number assigned to each square in a board, from 0 to 63.

secret squares - A list of the square numbers of all the light blue squares from the random board function.

clicked squares / squares - A list containing the square numbers of all the squares the user clicked.

red squares / bad clicks - A list containing the square numbers of all the squares the
user clicked which are not part of the secret squares
"""

# Importing all the classes from the appropriate files.
from turtle import Screen, onscreenclick, Turtle
from game_board import GameBoard
import time
from write import Writer
from threading import Timer
from game_brain import GameBrain
from wait_time import WaitTurtle

# Instancing the Screen class from the turtle module, turning off animation *tracer(0)* and setting screensize
window = Screen()
window.tracer(0)
window.screensize(canvwidth=800, canvheight=800, bg="black")

# Instancing Writer and WaitTurtle classes (these are classes that I made)
writer_turtle = Writer()
wait_turtle = WaitTurtle(window)

# Instancing GameBoard and GameBrain classes (these are classes that I made), passing in the appropriate arguments.
# NOTE: GameBoard class creates a game board & random board when instantiated, so I do not need to call extra functions.
game_board = GameBoard(writer_turtle)
game_brain = GameBrain(game_board=game_board, writer=writer_turtle, window=window, wait_turtle=wait_turtle)

# Calling functions from the GameBoard class. Creating a Turtle mask and then hiding it, and updating the window.
# NOTE: window.update() is a required function to see the screen when you have no animation (or tracer(0))
game_board.create_mask()
game_board.mask_hide()
window.update()

# A game board is visible, the mask is created but hidden. I wait ten seconds with the WaitTurtle class,
# letting the player memorise the squares, then show the mask and update the window.
wait_turtle.wait_time(10)
game_board.mask_show()
window.update()

# I call the onscreenclick() function that I imported from the turtle module.
# I pass in the clicked() function from the GameBrain class as an argument.
# Then I listen for screen clicks or any inputs with the mainloop() function.
onscreenclick(game_brain.clicked)
window.mainloop()
