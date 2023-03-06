#!/usr/bin/python3

# This is the "neocube" script "sw_cube.py" based on the python port "cubebit.py".
# The python script works on all newer Raspberry Pi (2/3/4/B/+), RPi Zero 1/2 
# with the "cubebit.py" python port for slices based on 4tronix neopixel cubes.
# It's just a sample to demo what's possible under use of our development "swc.py".
# "swc.py" is our own class symplifing squares and cubes.

# author        : Swen Hopfe
# created       : 22-01-10
# last modified : 22-02-18
#
# modified      : 22-05-22 by lpe, derived from sw_cube.py

#--------------------------------------------------------------------------------

import cubebit as cb
import swc as cbs
import time
import random
import sys,os

side = 5
brightness = 14
cb.create(side,brightness)
cbs.init(side)

red    = cb.fromRGB(128,0,0)
orange = cb.fromRGB(134,55,0)
citro  = cb.fromRGB(110,128,0)
yellow = cb.fromRGB(140,110,0)
green  = cb.fromRGB(0,128,0)
petrol = cb.fromRGB(0,110,110)
blue   = cb.fromRGB(0,0,128)
purple = cb.fromRGB(110,0,110)

black  = cb.fromRGB(0,0,0)
white  = cb.fromRGB(90,90,90)
grey1  = cb.fromRGB(40,40,55)
grey2  = cb.fromRGB(10,10,25)

cl_rb  = list([red, orange, yellow, citro, green, petrol, blue, purple, grey1, white])

#--------------------------------------------------------------------------------

def set_single_pixel():
    #Pixel
    #setpix(nx,ny,nz,cl)
    cbs.setpix(0, 0, 0, green)
    cb.show()
    time.sleep(3)
    cb.clear()

def set_number(num,col):
    #Nummer
    #cbs.number(num,z-deepness,cl)
    cbs.number(num, 1, col)
    cb.show()
    time.sleep(3)
    cb.clear()


def set_line():
    #Linie, Orientierung ori (0,1,2 entlang x,y,z-Achse), 2D-Koordinaten ko1,ko2 (0..(side-1), Beginn st, Laenge le, Farbe cl)  
    #line(ori,ko1,ko2,st,le,cl)
    cbs.line(2, 1, 1, 1, 2, white)
    #cbs.line(1,i,0,0,5,col)
    cb.show()
    time.sleep(3)
    cb.clear()

def set_vq_area():
    #Quadratflaeche, Orientierung ori (0,1,2 entlang xy,xz,yz-Ebene), Ebene lev (0..(side-1), Beginn1 st1, Beginn2 st2, Kantenlaenge le, Farbe cl)  
    #slice(ori,lev,st1,st2,le,cl)
    cbs.slice(0, 0, 1, 2, 2, white)
    cb.show()
    time.sleep(3)
    cb.clear()


def set_hq_area():
    #Quadrat, Orientierung ori (0,1,2 entlang xy,xz,yz-Ebene), Ebene lev (0..(side-1), Beginn1 st1, Beginn2 st2, Kantenlaenge le, Farbe cl)  
    #square(ori,lev,st1,st2,le,cl)
    cbs.square(1, 0, 1, 2, 3, white)
    cb.show()
    time.sleep(3)
    cb.clear()

def set_quader():
    #Wuerfel, ausgefuellt, Offset x,y,z, Kantenlaenge le, Farbe cl
    #fcube(ox, oy, oz, le, cl)
    cbs.fcube(0, 0, 0, side, white)
    cb.show()
    time.sleep(3)
    cb.clear()


def play_simple_demos():

    #set_single_pixel()
    #set_number()
    #set_line()
    #set_vq_area()
    #set_hq_area()
    #set_quader()

    #cbs.h_n_0(0,purple)
    #cbs.number(2, 4, purple)
    #cbs.h_number(1, 4, purple)
    #cbs.h_number(2, 4, purple)
    #cbs.h_number(3, 4, purple)
    #cbs.h_number(4, 4, purple)
    cbs.h_number(9, 4, purple)

    #cbs.line(1,i,0,0,5,col)
    # x 
    #cbs.line(0, 0, 0, 0, 5, white)
    # y
    #cbs.line(1, 0, 0, 0, 5, white)
    # z
    #cbs.line(2, 0, 0, 0, 5, white)

    cb.show()
    time.sleep(4)
    #cb.clear()
    cb.cleanup()


#--------------------------------------------------------------------------------

def rainbow():
     # rainbow

     cb.rainbow()
     cb.show()

     time.sleep(3)


def col_slices(col):
     # white slices

     for i in range(side):
       cbs.slice(2,i,0,0,side,col)
       cb.show()
       time.sleep(0.08)
       cbs.slice(2,i,0,0,side,black)
       cb.show()

     time.sleep(0.2)

     for i in range(side):
       cbs.slice(2,i,0,0,side,grey1)
       cb.show()
       time.sleep(0.04)
       cb.show()

     time.sleep(0.5)

     for i in range(side):
       cbs.slice(2,i,0,0,side,grey2)
       cb.show()
       time.sleep(0.02)
       cb.show()

     time.sleep(0.8)


def squares_up(col):
     # green squares

     for i in range(side):
       cbs.square(0,i,0,0,side,col)
       cb.show()
       time.sleep(0.25)

     time.sleep(1)
     cb.clear()


def squares_down(col):
     # blue squares

     for i in range(side):
       cbs.square(0,(4-i),0,0,side,cb.fromRGB((i*20),0,128))
       cb.show()
       time.sleep(0.15)

     time.sleep(1.5)



def numbers():
     # numbers

     i = 0
     for i in range(10):

       cl = white
       if (i > 0): cl = yellow
       if (i > 1): cl = citro
       if (i > 2): cl = green
       if (i > 3): cl = petrol
       if (i > 4): cl = blue
       if (i > 5): cl = purple
       if (i > 6): cl = red
       if (i > 7): cl = orange
       if (i > 8): cl = grey1
       d = 0
       for d in range(side):

          cbs.number(i, d, cl)
          cb.show()
          time.sleep(0.02)
          if (d == 3): time.sleep(0.05)
          if (d == 2): time.sleep(0.1)
          if (d == 1): time.sleep(0.2)
          if (d == 0): time.sleep(0.5)
          cb.clear()

     time.sleep(1)


def col_lines(col):
     # red lines

     for i in range(side):
       cbs.line(1,i,0,0,5,col)
       cbs.line(1,0,i,0,5,col)
       cbs.line(1,(4-i),4,0,5,col)
       cbs.line(1,4,(4-i),0,5,col)
       cb.show()
       time.sleep(0.25)

     for i in range(side-1):
       cbs.line(1,(i+1),1,0,5,col)
       cbs.line(1,1,(i+1),0,5,col)
       cbs.line(1,(3-i),3,0,5,col)
       cbs.line(1,3,(3-i),0,5,col)
       cb.show()
       time.sleep(0.15)

     cbs.line(1,2,2,0,5,col)
     cb.show()

     time.sleep(1)
     cb.clear()


def spinner(col):
     # spinner

     for sc in range(12):
       iz = 0
       ix = 0
       for ix in range(side):
          cbs.setpix(ix,0,iz,col)
          cbs.setpix(ix,(side-1),iz,col)
          cb.show()
          time.sleep(0.01)
          cb.clear()
       iz = 0
       ix = (side-1)
       for iz in range(side):
          cbs.setpix(ix,0,iz,col)
          cbs.setpix(ix,(side-1),iz,col)
          cb.show()
          time.sleep(0.01)
          cb.clear()
       iz = (side-1)
       ix = 0
       for ix in range(side):
          cbs.setpix(side-1-ix,0,iz,col)
          cbs.setpix(side-1-ix,(side-1),iz,col)
          cb.show()
          time.sleep(0.01)
          cb.clear()
       ix = 0
       iz = 0
       for iz in range(side):
          cbs.setpix(ix,0,side-1-iz,col)
          cbs.setpix(ix,(side-1),side-1-iz,col)
          cb.show()
          time.sleep(0.01)
          cb.clear()




def col_cube(col):
     # yellow cube

     cbs.line(0,0,0,0,5,col)
     cbs.line(0,4,0,0,5,col)

     cbs.line(0,0,4,0,5,col)
     cbs.line(0,4,4,0,5,col)

     cbs.line(1,0,0,0,5,col)
     cbs.line(1,4,0,0,5,col)

     cbs.line(1,0,4,0,5,col)
     cbs.line(1,4,4,0,5,col)

     cbs.line(2,0,0,0,5,col)
     cbs.line(2,4,0,0,5,col)

     cbs.line(2,0,4,0,5,col)
     cbs.line(2,4,4,0,5,col)
     cb.show()

     time.sleep(3)


def purple_rain():
    # purple rain
    cbs.purplerain()


def play_default_demo():
    while True:

        # rainbow

        cb.rainbow()
        cb.show()

        time.sleep(3)

        # white slices

        for i in range(side):
          cbs.slice(2,i,0,0,side,white)
          cb.show()
          time.sleep(0.08)
          cbs.slice(2,i,0,0,side,black)
          cb.show()

        time.sleep(0.2)

        for i in range(side):
          cbs.slice(2,i,0,0,side,grey1)
          cb.show()
          time.sleep(0.04)
          cb.show()

        time.sleep(0.5)

        for i in range(side):
          cbs.slice(2,i,0,0,side,grey2)
          cb.show()
          time.sleep(0.02)
          cb.show()

        time.sleep(0.8)

        # green squares

        for i in range(side):
          cbs.square(0,i,0,0,side,green)
          cb.show()
          time.sleep(0.25)

        time.sleep(1)
        cb.clear()

        # numbers

        i = 0
        for i in range(10):

          cl = white
          if (i > 0): cl = yellow
          if (i > 1): cl = citro
          if (i > 2): cl = green
          if (i > 3): cl = petrol
          if (i > 4): cl = blue
          if (i > 5): cl = purple
          if (i > 6): cl = red
          if (i > 7): cl = orange
          if (i > 8): cl = grey1
          d = 0
          for d in range(side):

             cbs.number(i, d, cl)
             cb.show()
             time.sleep(0.02)
             if (d == 3): time.sleep(0.05)
             if (d == 2): time.sleep(0.1)
             if (d == 1): time.sleep(0.2)
             if (d == 0): time.sleep(0.5)
             cb.clear()

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
          time.sleep(0.25)

        for i in range(side-1):
          cbs.line(1,(i+1),1,0,5,red)
          cbs.line(1,1,(i+1),0,5,red)
          cbs.line(1,(3-i),3,0,5,red)
          cbs.line(1,3,(3-i),0,5,red)
          cb.show()
          time.sleep(0.15)

        cbs.line(1,2,2,0,5,red)
        cb.show()

        time.sleep(1)
        cb.clear()

        # spinner

        for sc in range(12):
          iz = 0
          ix = 0
          for ix in range(side):
             cbs.setpix(ix,0,iz,petrol)
             cbs.setpix(ix,(side-1),iz,petrol)
             cb.show()
             time.sleep(0.01)
             cb.clear()
          iz = 0
          ix = (side-1)
          for iz in range(side):
             cbs.setpix(ix,0,iz,petrol)
             cbs.setpix(ix,(side-1),iz,petrol)
             cb.show()
             time.sleep(0.01)
             cb.clear()
          iz = (side-1)
          ix = 0
          for ix in range(side):
             cbs.setpix(side-1-ix,0,iz,petrol)
             cbs.setpix(side-1-ix,(side-1),iz,petrol)
             cb.show()
             time.sleep(0.01)
             cb.clear()
          ix = 0
          iz = 0
          for iz in range(side):
             cbs.setpix(ix,0,side-1-iz,petrol)
             cbs.setpix(ix,(side-1),side-1-iz,petrol)
             cb.show()
             time.sleep(0.01)
             cb.clear()

        # white slices

        for i in range(side):
          cbs.slice(2,i,0,0,side,white)
          cb.show()
          time.sleep(0.08)
          cbs.slice(2,i,0,0,side,black)
          cb.show()

        time.sleep(0.2)

        for i in range(side):
          cbs.slice(2,i,0,0,side,grey1)
          cb.show()
          time.sleep(0.05)
          cb.show()

        time.sleep(0.5)

        for i in range(side):
          cbs.slice(2,i,0,0,side,grey2)
          cb.show()
          time.sleep(0.02)
          cb.show()

        time.sleep(3)
        cb.clear()

        # yellow cube

        cbs.line(0,0,0,0,5,yellow)
        cbs.line(0,4,0,0,5,yellow)

        cbs.line(0,0,4,0,5,yellow)
        cbs.line(0,4,4,0,5,yellow)

        cbs.line(1,0,0,0,5,yellow)
        cbs.line(1,4,0,0,5,yellow)

        cbs.line(1,0,4,0,5,yellow)
        cbs.line(1,4,4,0,5,yellow)

        cbs.line(2,0,0,0,5,yellow)
        cbs.line(2,4,0,0,5,yellow)

        cbs.line(2,0,4,0,5,yellow)
        cbs.line(2,4,4,0,5,yellow)
        cb.show()

        time.sleep(3)

        # purple rain

        cbs.purplerain()

        # rainbow

        cb.rainbow()
        cb.show()
        time.sleep(3)
        cb.clear()

        # ====================   PLI ========================================================
        color_planes_h(1)
        color_planes_v(3)
        cbs.col_rain(blue)

        cbs.colorWipe(green)  # Green wipe
        cbs.colorWipe(yellow)  # Green wipe
        cbs.theaterChase(blue)  # Blue theater chase
        cbs.rainbow_lin()
        cbs.rainbowCycle()
        cbs.theaterChaseRainbow(120)

        cb.cleanup()


def color_planes_h(nr=1):
    # 1
    if nr == 1:
        cb.setPlane(side-1, 2, yellow)
        cb.setPlane(side-2, 2, green)
        cb.setPlane(side-3, 2, red)
        cb.setPlane(side-4, 2, purple)
        cb.setPlane(side-5, 2, blue)

    # 2
    elif nr == 2:
        cb.setPlane(side-1, 2, white)
        cb.setPlane(side-2, 2, orange)
        cb.setPlane(side-3, 2, yellow)
        cb.setPlane(side-4, 2, citro)
        cb.setPlane(side-5, 2, green)

    # 3
    elif nr == 3:
        cb.setPlane(side-1, 2, green)
        cb.setPlane(side-2, 2, red)
        cb.setPlane(side-3, 2, purple)
        cb.setPlane(side-4, 2, petrol)
        cb.setPlane(side-5, 2, blue)

    cb.show()
    time.sleep(3)


def color_planes_v(nr=1):
    # 1
    if nr == 1:
        cb.setPlane(side-1, 1, yellow)
        cb.setPlane(side-2, 1, green)
        cb.setPlane(side-3, 1, red)
        cb.setPlane(side-4, 1, purple)
        cb.setPlane(side-5, 1, blue)

    # 2
    elif nr == 2:
        cb.setPlane(side-1, 1, white)
        cb.setPlane(side-2, 1, orange)
        cb.setPlane(side-3, 1, yellow)
        cb.setPlane(side-4, 1, citro)
        cb.setPlane(side-5, 1, green)

    # 3
    elif nr == 3:
        cb.setPlane(side-1, 1, green)
        cb.setPlane(side-2, 1, red)
        cb.setPlane(side-3, 1, purple)
        cb.setPlane(side-4, 1, petrol)
        cb.setPlane(side-5, 1, blue)

    cb.show()
    time.sleep(3)



def rainbow_colors():
    maxIdxB = int(len(cl_rb))
    intv    = int(cb.numPixels()/maxIdxB)

    #print("max LEDS: %s" % cb.numPixels())
    #print("max colo: %s" % maxIdxB)
    #print("interval: %s" % intv)

    for i in range(intv):
        for j in range(maxIdxB):

            n = maxIdxB*i + j

            #print("i: %s -- j: %s ## n: %s" % (i,j,n))
            if n < cb.numPixels():
                cb.setPixel(n  ,cl_rb[j])

    for i in range(intv):
        n = i+120
        if n < cb.numPixels():
            cb.setPixel(n  ,cl_rb[i])

    cb.show()


#--------------------------------------------------------------------------------

if __name__ == "__main__":

    try:
        play_default_demo()


        #cbs.colorWipe(green)  # Green wipe
        #cbs.theaterChase(blue)  # Blue theater chase
        #cbs.rainbow_lin()
        cbs.rainbowCycle()
        #cbs.theaterChaseRainbow(120)

        #play_simple_demos()

        #rainbow()

        #rainbow_colors()

        #cb.cleanup()

        # single demos
        #col_slices(white)
        #col_slices(purple)
        #squares_up(green)
        #squares_down(citro)
        #numbers()
        #col_lines(red)
        #spinner(petrol)
        #col_cube(yellow)
        #purple_rain()
        #cbs.col_rain(blue)

        color_planes_h(1)
        color_planes_v(3)

        #cb.cleanup()

    except KeyboardInterrupt:
        print('execution stopped')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


