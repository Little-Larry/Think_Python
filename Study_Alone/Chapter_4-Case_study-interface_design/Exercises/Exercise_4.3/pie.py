# pie.py
# by Lawrence X. Amlord
# Apr 13th, 2014
# Xi'an, China
# GNU GPLv3 (http://www.gnu.org/licenses/gpl.html)

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def isosceles_triangle(turtle, side_length, point_angle):
    base_angle = 90.0 - (point_angle / 2.0)
    point_radians = point_angle / 360.0 * 2.0 * math.pi
    base_length = side_length * (math.sin(point_radians))
    fd(turtle, side_length)
    lt(turtle, 180.0 - base_angle)
    fd(turtle, base_length)
    lt(turtle, 180.0 - base_angle)
    fd(turtle, side_length)
    lt(turtle, 180.0 - point_angle)

def pie(turtle, n, radius):
    point_angle = 360.0 / n
    lt(turtle, 90.0)
    for i in range(n):
        isosceles_triangle(turtle, radius, point_angle)
        lt(turtle, point_angle)

def move_forward(turtle, length):
    """move the turtle forward without leaving any trail"""
    pu(turtle)
    fd(turtle, length)
    pd(turtle)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1

# draw a sequence of three flowers, as shown in the book
move_forward(bob, -100)
pie(bob, 5, 50)
die(bob)

jim = Turtle()
jim.delay = 0.1
pie(jim, 6, 50)
die(jim)

paul = Turtle()
paul.delay = 0.1
move_forward(paul, 100)
pie(paul, 7, 50)
die(paul)

# dump the content of the campus to the file canvas.eps
world.canvas.dump()

wait_for_user()
