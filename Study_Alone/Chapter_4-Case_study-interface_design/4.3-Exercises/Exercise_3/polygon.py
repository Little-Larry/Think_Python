# polygon.py
# from Think Python section 4.3
# edited by Lawrence X. Amlord
# Apr 12th, 2014
# Xi'an, China

from swampy.TurtleWorld import *

world = TurtleWorld()
def polygon(t, length, n):
    bob = t()
    degree = 360 / n
    for i in range(n):
        fd(bob, length)
        lt(bob, degree)

polygon(Turtle, 50, 8)

wait_for_user()
