# polygon.py

"""
This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def square(turtle, length):
    """
    draw a square with sides of the given length
    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        fd(turtle, length)
        lt(turtle)

def polyline(turtle, n, length, angle):
    """
    draw n line segments

    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(turtle, length)
        lt(turtle, angle)

def polygon(turtle, n, length):
    """
    Draws a polygon with the given number of sides.

    n: number of sides
    length: length of each side
    """
    angle = 360.0 / n
    polyline(turtle, n, length, angle)

def arc(turtle, radius, angle):
    """
    draw an arc with the given radius and angle

    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * radius * ((abs(angle)) / 360.0)
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # make a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(turtle, step_angle/2)
    polyline(turtle, n, step_length, step_angle)
    rt(turtle, step_angle/2)

def circle(turtle, radius):
    """
    draw a circle with the given radius
    """
    arc(turtle, radius, 360)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    world = TurtleWorld()

    bob = Turtle()
    bob.delay = 0.001

    #draw a circle centered on the origin
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)

    wait_for_user()
