# square.py
# from Think Python section 4.3
# edited by Lawrence X. Amlord
# Apr 12th, 2014
# Xi'an, China

from swampy.TurtleWorld import *

world = TurtleWorld()
def square(t):
    bob = t()
    for i in range(4):
        fd(bob, 100)
        lt(bob)

square(Turtle)

wait_for_user()
