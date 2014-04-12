# mypolygon2.py
# from Think Python section 4.2
# edited by Lawrence X. Amlord
# Apr 12th, 2014
# Xi'an, China

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

for i in range(4):
    print 'Hello!'

for i in range(4):
    fd(bob, 100)
    lt(bob)

wait_for_user()
