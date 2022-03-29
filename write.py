# Import the Turtle class from the turtle module.
from turtle import Turtle


class Writer(Turtle):
    """Turtle responsible for writing text on screen, including a current level count and a "GAME OVER" screen. """
    def __init__(self):
        """Instances the Turtle class (making this essentially a Turtle class you can edit as a class and sets the
        Turtles color to white. """
        super().__init__()
        self.color("white")

    def write_level(self, level):
        """Takes in a leve as a parameter, will write "Level: [LEVEL]" in the top left corner of the board.

        :param level: Current level
        :return: None
        """
        self.pu()
        self.hideturtle()
        self.goto(-395, 400)
        self.clear()
        self.pd()
        self.write("Level: " + str(level), False, "Left", ("Arial", 20, "normal"))

    def level_up(self, level):
        """Will clear the Turtle's writing and call the write_level() function, sending the level parameter passed
        into this function into the write_level() function

        :param level: Current level
        :return:
        """
        self.clear()
        self.write_level(level)

    def lost_the_game(self, level):
        """Sends the user to a "GAME OVER" screen, takes in a level and will also display the final level.

        :param level: Current level
        :return:
        """
        self.pu()
        self.hideturtle()
        self.goto(0, 0)
        self.clear()
        self.write("GAME OVER", False, "Center", ("Comic Sans MS", 60, "bold"))
        self.goto(0, -100)
        self.write("Final Level: " + str(level), False, "Center", ("Comic Sans MS", 20, "normal"))

