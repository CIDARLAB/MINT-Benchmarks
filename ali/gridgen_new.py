#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import string
import random
import math

def printnodes(grid_size, f):
    f.write("PORT ")
    for i in range(1,grid_size+1):
        f.write("nl"+str(i)+", nr"+str(i)+", nt"+str(i)+", nb"+str(i))
        if i!=grid_size:
            f.write(", ")
    f.write(" r = 100 ")
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

def printverticalvalves(grid_size,f):
    for i in range(1,grid_size):
        for j in range(1,grid_size+1):
            tar = "ct"+str(i)+"_"+str(j)
            src = "ct"+str(i+1)+"_"+str(j)
            f.write("VALVE vv"+str(i)+"_"+str(j)+" on ch_"+src+"_"+tar +" w=150 l=100;")
            newline(f)

def printhorizontalvalves(grid_size,f):
    for i in range(1, grid_size+1):
        for j in range(1,grid_size):
            src = "ct"+str(i)+"_"+str(j)
            tar = "ct"+str(i)+"_"+str(j+1)
            f.write("VALVE vh"+str(i)+"_"+str(j)+" on ch_"+src+"_"+tar +" w=100 l=150;")
            newline(f)        

def printverticalcontrolchannels(grid_size, f):
    #Creates ports in between all the cell traps
    for j in range(1, grid_size):
        f.write("PORT port_cntrlvalve_vertical_left_" + str(j) + " , " + "port_cntrlvalve_vertical_right_" + str(j) + " r=100;")
        newline(f)
        src = "port_cntrlvalve_vertical_left_" + str(j)
        tar = "vv1_" + str(j)
        f.write("CHANNEL ch_"+ src + "_" + tar + " from " + src + " 2 to " + tar + " 4 w=100;")
        newline(f)
        src = "port_cntrlvalve_vertical_right_" + str(j)
        tar = "vv" + str(grid_size) +"_" + str(j)
        f.write("CHANNEL ch_"+ src + "_" + tar + " from " + src + " 4 to " + tar + " 2 w=100;")
        newline(f)


grid_size = input("Enter Grid Size: ");
grid_size = int(grid_size)
device_name = "xgrid_" + str(grid_size);
f = open(device_name + ".uf", 'w');

f.write("DEVICE " + device_name + "\n");
newline(f);
f.write("LAYER FLOW\n");

printctgrid(grid_size, f)
newline(f)

printnodes(grid_size, f)
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

f.write("LAYER CONTROL")
newline(f)

printhorizontalvalves(grid_size,f)
newline(f)

printverticalvalves(grid_size,f)
newline(f)

printverticalcontrolchannels(grid_size, f)
newline(f)

f.write("END LAYER")
newline(f)

f.close();
