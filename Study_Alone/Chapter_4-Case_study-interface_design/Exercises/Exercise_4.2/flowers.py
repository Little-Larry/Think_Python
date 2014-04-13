# flowers.py

"""
This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

from polygon import *

def petal(turtle, radius, angle):
    """draw petal of two arcs
    radius: radius of arcs
    angle: angle of arcs
    """
    for i in range(2):
        arc(turtle, radius, angle)
        lt(turtle, 180 - angle)

def flower(turtle, n, radius, angle):
    """ draw a flower with given amount of petal
    n: amount of pertal
    raduis: radius of the petal arcs
    angle: angle of petal arcs
    """
    for i in range(n):
        petal(turtle, radius, angle)
        lt(turtle, 360.0 / n)

def move_forward(turtle, length):
    """move the turtle forward without leaving any trail"""
    pu(turtle)
    fd(turtle, length)
    pd(turtle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

# draw a sequence of three flowers, as shown in the book
move_forward(bob, -100)
flower(bob, 7, 60.0, 60.0)

move_forward(bob, 100)
flower(bob, 10, 40.0, 80.0)

move_forward(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)

# dump the content of the campus to the file canvas.eps
world.canvas.dump()

wait_for_user()
