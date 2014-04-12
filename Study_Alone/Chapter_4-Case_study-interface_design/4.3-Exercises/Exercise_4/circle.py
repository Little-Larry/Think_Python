# circle.py
# from Think Python section 4.3
# edited by Lawrence X. Amlord
# Apr 12th, 2014
# Xi'an, China

import math
from swampy.TurtleWorld import *

world = TurtleWorld()

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 60
    length = circumference / n
    polygon(t, length, n)

def polygon(t, length, n):
    bob = t()
    bob.delay = 0.01
    degree = 360 / n
    for i in range(n):
        fd(bob, length)
        lt(bob, degree)

circle(Turtle, 10)
circle(Turtle, 20)
circle(Turtle, 40)
circle(Turtle, 80)
wait_for_user()
