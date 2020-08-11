# -*- coding: utf-8 -*-
from graphics import *
from math import sqrt
length = int(input("Enter window length: "))
spacing = int(input("Enter shape spacing: "))

# Create graphics window
win = GraphWin('Art', length, length)

width = (length - (3 * spacing)) / 2
x0 = spacing
y0 = (length - width) / 2
      
#Bottom left, top left, top right, and bottom right of square face
p0 = Point(x0, y0)
p1 = Point(x0, y0 + width)
p2 = Point(x0 + width, y0 + width)
p3 = Point(x0 + width, y0)

frontface1 = Polygon([p0,p1,p2,p3])

#Choose color
frontface1.setFill('pink')
frontface1.draw(win)

#top side of cube
t0 = Point(x0, y0)
t1 = Point(x0 + width*sqrt(2)/2, y0 - width*sqrt(2)/2)
t2 = Point(x0 + width*sqrt(2)/2 + width, y0 - width*sqrt(2)/2)
t3 = Point(x0 + width, y0)

topface1 = Polygon([t0,t1,t2,t3])

#Choose color
topface1.setFill('red')
topface1.draw(win)


#side of the cube
s0 = Point(x0 + width*sqrt(2)/2 + width, y0 - width*sqrt(2)/2 + width)

#using points from previous cube faces
sideface1 = Polygon([p2,t3,t2,s0])

#Choose color
sideface1.setFill('red')
sideface1.draw(win)

#Prism code below
x0 = 2 * spacing + width
y0 = (length - width) / 2

#front of prism
f0 = Point(x0, y0)
f1 = Point(x0 + width, y0 + width)
f2 = Point(x0, y0 + width)

frontface2 = Polygon([f0,f1,f2])

#Choose color
frontface2.setFill('lightgreen')
frontface2.draw(win)

#Side of prism
j0 = Point(x0, y0)
j1 = Point(x0 + width*sqrt(2)/2, y0 - width*sqrt(2)/2)
j2 = Point(x0 + width*sqrt(2)/2 + width, y0 - width*sqrt(2)/2 + width)
j3 = Point(x0 + width, y0 + width)

sideface2 = Polygon([j0,j1,j2,j3])

#Choose color
sideface2.setFill('green')
sideface2.draw(win)



# Close after mouse click
try:
    win.getMouse()    
    win.close()
except:
    pass