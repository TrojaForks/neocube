#!/usr/bin/python

# This is the "neocube"script sw_cube.py based on the python port cubebit.py.
# The python script works on any newer Raspberry Pi (and RPi Zero 1 and 2) with the cubebit.py python port for slices based on 4tronix neopixel cubes.
# It's just a sample to demo what's possible under use of our development swc.py.
# swc.py is our own class much more symplifing squares and cubes.

# author        : Swen Hopfe
# created       : 19-03-21
# last modified : 22-02-10

#--------------------------------------------------------------------------------

import cubebit as cb
import swc as cbs 
import time
import random

side = 5
brightness = 25
cb.create(side,brightness)
cbs.init(side)

black  = cb.fromRGB(0,0,0)
white  = cb.fromRGB(90,90,90)
grey1  = cb.fromRGB(40,40,55)
grey2  = cb.fromRGB(10,10,25)
yellow = cb.fromRGB(140,110,0)
green = cb.fromRGB(0,128,0)
blue = cb.fromRGB(0,0,128)
red = cb.fromRGB(128,0,0)


#--------------------------------------------------------------------------------

#Linie, Orientierung ori (0,1,2 entlang x,y,z-Achse), 2D-Koordinaten ko1,ko2 (0..(side-1), Beginn st, Laenge le, Farbe cl)  
#line(ori,ko1,ko2,st,le,cl)

#cbs.line(2, 1, 1, 1, 2, white)
#cbs.line(2, 2, 1, 1, 2, yellow)

#Quadratflaeche, Orientierung ori (0,1,2 entlang xy,xz,yz-Ebene), Ebene lev (0..(side-1), Beginn1 st1, Beginn2 st2, Kantenlaenge le, Farbe cl)  
#slice(ori,lev,st1,st2,le,cl)

#cbs.slice(0, 0, 1, 2, 2, white)
#cbs.slice(0, 1, 1, 2, 2, yellow)

#Quadrat, Orientierung ori (0,1,2 entlang xy,xz,yz-Ebene), Ebene lev (0..(side-1), Beginn1 st1, Beginn2 st2, Kantenlaenge le, Farbe cl)  
#square(ori,lev,st1,st2,le,cl)

#cbs.square(1, 0, 1, 2, 3, white)
#cbs.square(1, 1, 1, 2, 3, yellow)

#Wuerfel, ausgefuellt, Offset x,y,z, Kantenlaenge le, Farbe cl
#fcube(ox, oy, oz, le, cl)

#cbs.fcube(0, 0, 0, side, white)
#cbs.fcube(0, 1, 2, 3, yellow)

#--------------------------------------------------------------------------------


# rainbow

cb.rainbow()
cb.show()

time.sleep(3)

# white slices 

for i in range(side):
   cbs.slice(2,i,0,0,side,white)
   cb.show()
   time.sleep(0.12)
   cbs.slice(2,i,0,0,side,black)
   cb.show()

time.sleep(0.2)

for i in range(side):
   cbs.slice(2,i,0,0,side,grey1)
   cb.show()
   time.sleep(0.06)
   cb.show()

time.sleep(0.5)

for i in range(side):
   cbs.slice(2,i,0,0,side,grey2)
   cb.show()
   time.sleep(0.03)
   cb.show()

time.sleep(0.8)

# green squares

for i in range(side):
   cbs.square(0,i,0,0,side,green)
   cb.show()
   time.sleep(0.35)

time.sleep(1)

# blue squares

for i in range(side):
   cbs.square(0,(4-i),0,0,side,cb.fromRGB((i*20),0,128))
   cb.show()
   time.sleep(0.15)

time.sleep(1.5)

# red lines

for i in range(side):
   cbs.line(1,i,0,0,5,red)
   cbs.line(1,0,i,0,5,red)
   cbs.line(1,(4-i),4,0,5,red)
   cbs.line(1,4,(4-i),0,5,red)
   cb.show()
   time.sleep(0.35)

for i in range(side-1):
   cbs.line(1,(i+1),1,0,5,red)
   cbs.line(1,1,(i+1),0,5,red)
   cbs.line(1,(3-i),3,0,5,red)
   cbs.line(1,3,(3-i),0,5,red)
   cb.show()
   time.sleep(0.2)

cbs.line(1,2,2,0,5,red)
cb.show()

time.sleep(0.8)

# white slices

for i in range(side):
   cbs.slice(2,i,0,0,side,white)
   cb.show()
   time.sleep(0.12)
   cbs.slice(2,i,0,0,side,black)
   cb.show()

time.sleep(0.2)

for i in range(side):
   cbs.slice(2,i,0,0,side,grey1)
   cb.show()
   time.sleep(0.06)
   cb.show()

time.sleep(0.5)

for i in range(side):
   cbs.slice(2,i,0,0,side,grey2)
   cb.show()
   time.sleep(0.03)
   cb.show()

time.sleep(1)

# yellow cubes

cbs.fcube(0, 1, 2, 3, yellow)
cb.show()

time.sleep(5) 

# purple rain

cbs.purplerain()

# rainbow

cb.rainbow()
cb.show()
time.sleep(3)

cb.clear() 

cb.cleanup()

#--------------------------------------------------------------------------------
