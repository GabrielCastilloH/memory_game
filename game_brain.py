
class GameBrain:
    """
    Controls when to call each function from each class.
    Creates click interactivity, checks if the player has won.
    """
    def __init__(self, game_board, writer, window, wait_turtle):
        """Responsible for creating all the attributes associated with this class,
        and accessing all the required classes for this class to work.

        :param game_board: GameBoard class
        :param writer: Writer class
        :param window: Window class
        :param wait_turtle: WaitTurtle class
        """
        self.game_board = game_board
        self.wait_turtle = wait_turtle
        self.levels = writer
        self.window = window
        self.clicked_squares = []
        self.bad_clicks = []

    def clicked(self, x, y):
        """Takes in x and y, find the square that was clicked on the mask board and changes the color to green or red.
        Depending on whether that square is part of the secret squares.

        :param x: x-coor of mouse click
        :param y: y-coor of mouse click
        :return: None
        """

        # Calculates the *square number* of the square the user clicked using the coordinates.
        column = (x + 400) // 100
        row = (-y + 400) // 100
        square_number = int(column + row * 8)

        # Checks if the length of the *clicked squares* list is less than 8 and if the *square number* that of the
        # square the user clicked is in not already in the list of *clicked squares*.
        if len(self.clicked_squares) < 8 and square_number not in self.clicked_squares:
            """This If statement is responsible for adding the *square number* of the squares the user clicks on. The 
            previously mentioned check is needed to prevent duplicate numbers and prevent the user from clicking more 
            than 8 times."""

            # If the previous statement is True, then the *square number* gets appended to the *clicked squares* list.
            self.clicked_squares.append(square_number)

            # The following is an algorithm to reverse the previously collected *square number* and change it
            # accordingly, since the *mask board* list is reversed.
            index_row = 7 - int(square_number / 8)
            index_column = 7 - square_number % 8
            if index_column == 0:
                index_column = 7
            else:
                index_column = 7 - index_column

            # Check if the *square number* is one of the *secret squares*, and then
            # access it using the variables collected from my algorithm.
            if square_number in self.game_board.secret_square:
                # If it is one of the *secret squares*, color it green.
                self.game_board.mask[index_row][index_column].color("green")
            else:
                # If it isn't one of the *secret squares*, color it red.
                self.game_board.mask[index_row][index_column].color("red")

                # Using the opposite of my algorithm, I get the square number of the *game board* and then append that
                # number to the bad clicks
                x, y = self.game_board.mask[index_row][index_column].pos()
                column = (x + 400) // 100
                row = (-y + 400) // 100
                square_number = int(column + row * 8)
                self.bad_clicks.append(square_number)
            self.window.update()

        # Check if the length of *clicked squares* is 8, and if it is call the GameBrain.won_lost() function.
        if len(self.clicked_squares) == 8:
            self.won_lost(self.check_if_won())

    def check_if_won(self):
        """Checks if all *clicked squares* are in the list of *secret squares*. Returns boolean.

        :return: True or False
        """
        for square in self.clicked_squares:
            if square not in self.game_board.secret_square:
                return False
        return True

    def won_lost(self, won):
        """Levels up player if they won, or throws "GAME OVER" screen if they lost.

        :param won: Function that checks whether the player has won.
        :return: None
        """

        # NOTE: won() function will automatically execute when it is passed as a parameter.

        # If/Else statement, will execute depending on what the function won() returns.
        if won:
            # If the player wins, the GameBoard.level_up() function will run.
            self.game_board.level_up(self.levels)
            self.game_board.mask_hide()

            # With the new random board created, the mask will hide for a time relative to the level.
            self.wait_turtle.wait_time(20/self.game_board.level + 1)

            # After that time, the mask will show, the window will update and the *squares* will be cleared.
            self.game_board.mask_show()
            self.window.update()
            self.clicked_squares.clear()
            return
        else:
            # NOTE: wait_time() function leaves animation turned off after executing.
            # If the player loses, wait two seconds, turn on animation, and then hide the *red squares*.
            self.wait_turtle.wait_time(2)
            self.window.tracer(1)
            self.game_board.mask_hide_all_but_red(self.bad_clicks)

            # After another 2 seconds, turn animation on, hide the mask (now revealing the blue squares again),
            # and clear the text on the screen
            self.wait_turtle.wait_time(2)
            self.window.tracer(1)
            self.game_board.mask_hide()
            self.levels.clear()

            # Call the GameBoard.lost_the_game() function, turn animation off, display "GAME OVER" and update the screen
            self.game_board.lost_the_game()
            self.window.tracer(0)
            self.levels.lost_the_game(self.game_board.level)
            self.window.update()
            return
