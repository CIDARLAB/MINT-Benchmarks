#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import string
import random
import math

def printnodes(grid_size, f):
    f.write("NODE ")
    for i in range(1,grid_size+1):
        f.write("nl"+str(i)+", nr"+str(i)+", nt"+str(i)+", nb"+str(i))
        if i!=grid_size:
            f.write(", ")
    f.write(";")
    newline(f)

def printctgrid(grid_size,f):
    f.write("SQUARE CELL TRAP ")
    for i in range(1,grid_size+1):
        for j in range(1,grid_size+1):
            f.write("ct"+str(i)+"_"+str(j))
            if not(i==grid_size and j==grid_size):
                f.write(', ')
    f.write(" chamberWidth=100 chamberLength=100 channelWidth=100;")
    newline(f)

def newline(f):
    f.write("\n")

def printtopchannels(grid_size, f):
    for i in range(1, grid_size+1):
        for j in range(1, grid_size+1):
            if i == 1:
                #Connect to the top nodes
                src = "ct"+str(i)+"_"+str(j)
                tar = "nt"+str(j)
                
            else:
                #Connect between cell traps
                src = "ct"+str(i)+"_"+str(j)
                tar = "ct"+str(i-1)+"_"+str(j)

            f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 1 to "+tar+" 3 w=100;")
            newline(f)

def printrightchannels(grid_size, f):
    for i in range(1, grid_size+1):
        for j in range(1, grid_size+1):
            if j == grid_size:
                #Connect to the top nodes
                src = "ct"+str(i)+"_"+str(j)
                tar = "nr"+str(i)
                
            else:
                #Connect between cell traps
                src = "ct"+str(i)+"_"+str(j)
                tar = "ct"+str(i)+"_"+str(j+1)

            f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 2 to "+tar+" 4 w=100;")
            newline(f)

def printleftchannels(grid_size, f):
    for i in range(1, grid_size+1):
        src = "ct"+str(i)+"_1"
        tar = "nl"+str(i)
        f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 4 to "+tar+" 2 w=100;")
        newline(f)

def printbottomchannels(grid_size, f):
    for j in range(1, grid_size+1):
        src = "ct"+str(grid_size)+"_"+str(j)
        tar = "nb"+str(j)
        f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 3 to "+tar+" 1 w=100;")
        newline(f)

def printhorizontalvalvenodes(grid_size,f):
    f.write("NODE ")
    for i in range(1,grid_size+1):
        f.write("cnhl"+str(i)+" , cnhr"+str(i))
        if not(grid_size == i):
            f.write(" , ")
    f.write(";")
    
def printhorizontalvalves(grid_size,f):
    for i in range(1, grid_size+1):
        for j in range(1,grid_size):
            src = "ct"+str(i)+"_"+str(j)
            tar = "ct"+str(i)+"_"+str(j+1)
            f.write("VALVE vh"+str(i)+"_"+str(j)+" on ch_"+src+"_"+tar +" w=100 l=150;")
            newline(f)

def printhorizontalvalvenet(grid_size,f):
    for i in range(1,grid_size+1):
        f.write("NET neth"+str(i)+" from " + "cnhl"+str(i)+ " 2 to ")
        for j in range(1,grid_size):
            f.write("vh"+str(i)+"_"+str(j)+" 3 , ")
        f.write("cnhr"+str(i)+" 4 channelWidth=50;")
        newline(f)

def printverticalvalvenodes(grid_size,f):
    f.write("NODE ")
    for j in range(1,grid_size):
        f.write("cnvl"+str(j)+" , cnvr"+str(j))
        if not(grid_size-1 == j):
            f.write(" , ")
    f.write(";")
        
def printverticalvalves(grid_size,f):
    for i in range(1,grid_size):
        for j in range(1,grid_size+1):
            tar = "ct"+str(i)+"_"+str(j)
            src = "ct"+str(i+1)+"_"+str(j)
            f.write("VALVE vv"+str(i)+"_"+str(j)+" on ch_"+src+"_"+tar +" w=150 l=100;")
            newline(f)

def printverticalvalverightchannels(grid_size,f):
    for i in range(1,grid_size):
        src = "cnvl"+str(i)
        tar = "vv"+str(i)+"_1"
        f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 2 to "+tar+" 4 w=50;")
        newline(f)
        for j in range(1,grid_size):
            src = "vv"+str(i)+"_"+str(j)
            tar = "vv"+str(i)+"_"+str(j+1)
            f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 2 to "+tar+" 4 w=50;")
            newline(f)
        tar = "cnvr"+str(i)
        src = "vv"+str(i)+"_"+str(grid_size)
        f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 2 to "+tar+" 4 w=50;")
        newline(f)
        
def printinterconnectionnodes(grid_size,f):
    for i in range(1, grid_size+1):
        for j in range(1,grid_size):
            f.write("NODE nh"+str(i)+"_"+str(j)+";")
            newline(f)

def printverticalicnodechannels(grid_size,f):
    for i in range(1, grid_size+1):
        for j in range(1,grid_size):
            src = "nh"+str(i)+"_"+str(j)
            tar = "vh"+str(i)+"_"+str(j)
            f.write("CHANNEL ch_nh"+str(i)+"_"+str(j)+" from "+src+" 1 to "+tar+" 3 w=50;")
            newline(f)

def printchannelsconnectingnodes(grid_size,f):
    for i in range(1,grid_size+1):
        src = "cnhl"+str(i)
        tar = "nh"+str(i)+"_1"
        f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 2 to "+tar+" 4 w=50;")
        newline(f)
        for j in range(1,grid_size-1):
            src = "nh"+str(i)+"_"+str(j)
            tar = "nh"+str(i)+"_"+str(j+1)
            f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 2 to "+tar+" 4 w=50;")
            newline(f)
        tar = "cnhr"+str(i)
        src = "nh"+str(i)+"_"+str(grid_size-1)
        f.write("CHANNEL ch_"+src+"_"+tar+" from "+src+" 2 to "+tar+" 4 w=50;")
        newline(f)

def setleftnodepositions(grid_size, f):
    xpos = 2500
    ypos = 2500
    for i in range(1, grid_size):
        src = "nl"+str(i)
        f.write(src + " SET X " + str(xpos) + " SET Y "+str(ypos)+ " ;")
        ypos = ypos + 1000
        newline(f)
        
                
def setleftcontrolleftnodes(grid_size, f):
    xpos = 2500
    ypos = 5000
    for i in range(1, grid_size):
        src =  "cnhl"+str(i)
        f.write(src + " SET X " + str(xpos) + " SET Y "+str(ypos)+ " ;")
        ypos = ypos + 1000
        newline(f)

grid_size = input("Enter Grid Size: ")
device_name = "grid_" + str(grid_size)
f = open(device_name + ".uf", 'w')

f.write("DEVICE " + device_name + "\n")
newline(f)
f.write("LAYER FLOW\n")

printctgrid(grid_size, f)
newline(f)

printnodes(grid_size, f)
newline(f)

setleftnodepositions(grid_size, f)
newline(f)

printtopchannels(grid_size, f)
newline(f)

printrightchannels(grid_size, f)
newline(f)

printleftchannels(grid_size, f)
newline(f)

printbottomchannels(grid_size, f)
newline(f)

f.write("END LAYER")
newline(f)
newline(f)

#Control Layer stuff
f.write("LAYER CONTROL\n");

printhorizontalvalvenodes(grid_size,f)
newline(f)

printhorizontalvalves(grid_size,f)
newline(f)


printinterconnectionnodes(grid_size,f)
newline(f)

printverticalicnodechannels(grid_size,f)
newline(f)

printchannelsconnectingnodes(grid_size,f)
newline(f)

#printhorizontalvalvenet(grid_size,f)
newline(f)

printverticalvalvenodes(grid_size,f)
newline(f)

printverticalvalves(grid_size,f)
newline(f)

printverticalvalverightchannels(grid_size,f)
newline(f)

setleftcontrolleftnodes(grid_size, f)
newline(f)

f.write("END LAYER")
newline(f)
f.close()
