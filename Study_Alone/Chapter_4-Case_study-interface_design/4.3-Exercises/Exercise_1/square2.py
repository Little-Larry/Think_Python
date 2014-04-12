# square2.py
# from Think Python section 4.3
# edited by Lawrence X. Amlord
# Apr 12th, 2014
# Xi'an, China

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)

square(bob)

wait_for_user()
