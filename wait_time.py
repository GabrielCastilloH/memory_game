# Import the Turtle class from the turtle module.
from turtle import Turtle


class WaitTurtle(Turtle):
    """
    A Turtle object that waits a certain amount of time by turning animation on, making itself (a Turtle) move
    forward for a certain amount of pixel depending on the seconds inputted to its wait_time() function.
    """

    def __init__(self, window):
        """Instances the Turtle class (making this essentially a Turtle class you can edit as a class, creates a
        self.window attribute to easily access the Screen class, puts its pen up and sets its speed to 1,
        which is the slowest, then hides itself.

        :param window: Screen class from turtle module
        """
        super().__init__()
        self.window = window
        self.pu()
        self.speed(1)
        self.hideturtle()

    def wait_time(self, secs):
        """Waits for the number of seconds passed through the use of animated movement of an invisible Turtle.

        :param secs: Number of seconds to wait for.
        :return: None
        """
        self.window.tracer(1)
        self.forward(secs * 250)
        self.window.tracer(0)
        return
