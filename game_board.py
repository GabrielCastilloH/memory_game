# Importing the Turtle object and the randint() function.
from turtle import Turtle
from random import randint

# POSITIONS constant variable. Locations the Turtle objects will move to, to create the board.
# It is a list of 8 lists, each list containing 8 tuples which contain two numbers used as locations.
POSITIONS = [
    [(-350, -350), (-250, -350), (-150, -350), (-50, -350), (50, -350), (150, -350), (250, -350), (350, -350)],
    [(-350, -250), (-250, -250), (-150, -250), (-50, -250), (50, -250), (150, -250), (250, -250), (350, -250)],
    [(-350, -150), (-250, -150), (-150, -150), (-50, -150), (50, -150), (150, -150), (250, -150), (350, -150)],
    [(-350, -50), (-250, -50), (-150, -50), (-50, -50), (50, -50), (150, -50), (250, -50), (350, -50)],
    [(-350, 50), (-250, 50), (-150, 50), (-50, 50), (50, 50), (150, 50), (250, 50), (350, 50)],
    [(-350, 150), (-250, 150), (-150, 150), (-50, 150), (50, 150), (150, 150), (250, 150), (350, 150)],
    [(-350, 250), (-250, 250), (-150, 250), (-50, 250), (50, 250), (150, 250), (250, 250), (350, 250)],
    [(-350, 350), (-250, 350), (-150, 350), (-50, 350), (50, 350), (150, 350), (250, 350), (350, 350)],
]


class GameBoard:
    """Creates an 8 by 8 board using Turtle objects. It's functions include the creation of a *game board*,
    *random board*, *mask board*, hiding/showing the *mask board*, leveling up the player, and hiding everything for
    when the user loses the game.

    """

    def __init__(self, writer):
        """Making attributes responsible for keeping track all the boards including: *game board*, *random board*,
        and *mask board*. Attributes are also responsible for keeping track of the player level and the *secret
        squares*. Automatically creates a *game board* and a *random board*.

        :param writer: Turtle object used for writing text on screen.
        """
        self.all_squares = [[], [], [], [], [], [], [], []]
        self.mask = [[], [], [], [], [], [], [], []]
        self.secret_square = []
        self.level = 1
        writer.level_up(self.level)
        self.create_board()
        self.create_ranboard()

    def create_board(self):
        """Creates a *game board*.

        :return: None
        """
        # Loops through the first 8 lists in the POSITIONS constant.
        for _ in range(len(POSITIONS)):
            # Loops through each of the tuples in the appropriate list in the POSITIONS constant.
            for i in range(len(POSITIONS[_])):
                # Creates a new turtle object, puts its pen up, colors it white, and changes the shape.
                new_square = Turtle("square")
                new_square.pu()
                new_square.color("white")
                new_square.turtlesize(4.8, 4.8)

                # Turtle goes to the coordinates in the currently looped at tuple in the POSITIONS constant and
                # gets appended to the *game board* list called all_squares.
                new_square.goto(POSITIONS[_][i])
                self.all_squares[_].append(new_square)

    def reset_board(self):
        """Changes the color of all the Turtles in the *game board* list called all_squares back to white.

        :return: None
        """
        for _ in range(len(self.all_squares)):
            for i in range(len(self.all_squares[_])):
                current_turt = self.all_squares[_][i]
                current_turt.color("white")

    def create_ranboard(self):
        """Creates a *random board*.

        :return: None
        """
        # Loops through the total number of lists in all_squares.
        for _ in range(len(self.all_squares)):

            # Generates a random number from 0-7 inclusive.
            random_num = randint(0, 7)

            # Loops through the total number of items in the current list that is in the previous loop.
            for i in range(len(self.all_squares[_])):
                if i == random_num:
                    # If the random number is the same as the index number of the square currently being looped through
                    # the square at this index will get changed to light blue (or cyan).
                    self.all_squares[_][i].color("cyan")

                    # Using the position of the secret square along with my algorithm, I find the *square number* for
                    # the square I am coloring cyan and append it to the *secret square* list.
                    x, y = self.all_squares[_][i].pos()
                    column = (x + 400) // 100
                    row = (-y + 400) // 100
                    square = int(column + row * 8)
                    self.secret_square.append(square)

    def create_mask(self):
        """Creates a *mask board*

        :return: None
        """
        # Using the method used to create the *game board*, this creates a *mask board*.
        for _ in range(len(POSITIONS)):
            for i in range(len(POSITIONS[_])):
                new_square = Turtle("square")
                new_square.pu()
                new_square.color("white")
                new_square.turtlesize(4.8, 4.8)
                new_square.goto(POSITIONS[_][i])

                # Instead of appending to the all_square lists, it gets appended to the mask list.
                self.mask[_].append(new_square)

    def mask_hide(self):
        """Hides all the turtles in the mask.

        :return: None
        """
        # Loops through all the Turtles in the *mask board* and hides each Turtle.
        for _ in range(len(self.mask)):
            for i in range(len(self.mask[_])):
                self.mask[_][i].ht()

    def mask_hide_all_but_red(self, bad_clicks):
        """Takes a list of *square numbers* and hides the other Turtles.

        :param bad_clicks: List containing the list of *square numbers* you want to stay visible.
        :return:
        """
        # Looping through each item of each list in the *mask board*.
        for _ in range(len(self.mask)):
            for i in range(len(self.mask[_])):

                # Obtains the *square number* of the Turtle that is currently being looped through.
                x, y = self.mask[_][i].pos()
                column = (x + 400) // 100
                row = (-y + 400) // 100
                square = int(column + row * 8)

                # Checks if the number is not in the *bad clicks* list, if it isn't it hides that Turtle.
                if square not in bad_clicks:
                    self.mask[_][i].ht()

    def mask_show(self):
        """Shows the mask while turning all Turtles in the *mask board* to the color white.

        :return: None
        """
        # Loops through all Turtles in the *mask board*, show them and change their color to white.
        for _ in range(len(self.mask)):
            for i in range(len(self.mask[_])):
                self.mask[_][i].color("white")
                self.mask[_][i].st()

    def level_up(self, writer):
        """Clears all lists and resets each of the boards, calling the Writer.level_up() function.

        :param writer: Writer class
        :return: None
        """
        # Increases the level variable by 1 and clears the *secret squares* list.
        self.level += 1
        self.secret_square.clear()

        # Calls the reset_board() function, creates a new *random board*, and calles the Writer.level_up() function.
        self.reset_board()
        self.create_ranboard()
        writer.level_up(self.level)

    def lost_the_game(self):
        """Loops through all the Turtles in *game board* and hides them.

        :return:
        """
        for _ in range(len(self.all_squares)):
            for i in range(len(self.all_squares[_])):
                current_turt = self.all_squares[_][i]
                current_turt.hideturtle()

