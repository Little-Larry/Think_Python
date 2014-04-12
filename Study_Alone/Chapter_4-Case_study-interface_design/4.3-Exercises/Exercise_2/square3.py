# square3.py
# from Think Python section 4.3
# edited by Lawrence X. Amlord
# Apr 12th, 2014
# Xi'an, China

from swampy.TurtleWorld import *

world = TurtleWorld()
def square(t, length):
    bob = t()
    for i in range(4):
        fd(bob, length)
        lt(bob)

square(Turtle, 50)
square(Turtle, 100)
square(Turtle, 150)

wait_for_user()
