#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import string
import random
import math


def newline(f):
    f.write("\n")

def writestatement(statement):
    f.write(statement)
    newline(f)

def fixposition(component_name , xoffset, yoffset):
    statement = component_name + " SET X " + str(xoffset) + " SET Y " + str(yoffset) + ";"
    writestatement(statement)

def printtopports(grid_size, f):
    for i in range(1, grid_size+1):
        statement = "PORT port_top_"+ str(i) + " r = 100 ; "
        writestatement(statement)

def printrightports(grid_size, f):
    for i in range(1, grid_size+1):
        statement = "PORT port_right_"+ str(i) + " r = 100 ; "
        writestatement(statement)

def printbottomports(grid_size, f):
    for i in range(1, grid_size+1):
        statement = "PORT port_bottom_"+ str(i) + " r = 100 ; "
        writestatement(statement)

def printleftports(grid_size, f):
    for i in range(1, grid_size+1):
        statement = "PORT port_left_"+ str(i) + " r = 100 ; "
        writestatement(statement)

def printcelltraps(grid_size, f):
    for x in range(1, grid_size+1):
        for y in range(1, grid_size+1):
            statement = "SQUARE CELL TRAP cell_trap_" + str(x) + "_" + str(y) + " chamberWidth=100 chamberLength=100 channelWidth=100 ; "
            writestatement(statement)

def getchannelname(src, tar):
    return "channel_"+ src + "_" + tar

def printchannel(src, src_term , tar, tar_term , width):
    statement = "CHANNEL channel_"+ src + "_" + tar + " from " + src + " " + str(src_term) +  " to " + tar + " " + str(tar_term) + " w = " + str(width) + " ;"
    writestatement(statement)


def printinsidechannels(grid_size, f):    
    for x in range(1, grid_size):
        for y in range(1, grid_size + 1):
            #Printing horizontal channels 
            src = "cell_trap_" + str(x) + "_" + str(y)
            tar = "cell_trap_" + str(x+1) + "_" + str(y)
            printchannel(src, 2, tar, 4, 100)

    for x in range(1, grid_size + 1):
        for y in range(1, grid_size):
            #Printing vertical channels 
            src = "cell_trap_" + str(x) + "_" + str(y)
            tar = "cell_trap_" + str(x) + "_" + str(y+1)
            printchannel(src, 3, tar, 1, 100)

def printoutsidechannels(grid_size, f):
    for i in range(1, grid_size+1):
        #Print channels from edge celltraps to ports)
        #Top port
        src = "port_top_"+ str(i)
        tar = "cell_trap_" + str(i) + "_" + str(1)
        printchannel(src, 3, tar, 1, 100)
        
        #Right Port
        src = "cell_trap_" + str(grid_size) + "_" + str(i)
        tar = "port_right_"+ str(i)
        printchannel(src, 2, tar, 4, 100)

        #Bottom Port
        src = "cell_trap_" + str(i) + "_" + str(grid_size)
        tar = "port_bottom_"+ str(i)
        printchannel(src, 3, tar, 1, 100)
        
        #Left Port
        src = "port_left_"+ str(i)
        tar = "cell_trap_" + str(1) + "_" + str(i)
        printchannel(src, 2, tar, 4, 100)


def printvalves(grid_size, f):
    #Horzontal Valves
    for x in range(1, grid_size):
        for y in range(1, grid_size+1):
            src = "cell_trap_" + str(x) + "_" + str(y)
            tar = "cell_trap_" + str(x+1) + "_" + str(y)
            channelname = getchannelname(src, tar)
            statement = "VALVE valve_horizontal_" + str(x) + "_"+ str(y) + " on " + channelname + " w = 100 l = 150 ;"
            writestatement(statement)
    
    #Vertical Valves
    for x in range(1, grid_size+1):
        for y in range(1, grid_size):
            src = "cell_trap_" + str(x) + "_" + str(y)
            tar = "cell_trap_" + str(x) + "_" + str(y+1)
            channelname = getchannelname(src, tar)
            statement = "VALVE valve_vertical_" +  str(x) + "_"+ str(y) + " on " + channelname + " w = 150 l = 100 ;"
            writestatement(statement)

def printhorizontalvalveports(grid_size, f):
    xoffset = 3000
    yoffset = 11330
    for i in range(1, grid_size+1):
        statement = "PORT port_horizontal_valve_left_" + str(i) + " r = 100; "
        writestatement(statement)
        #Fixing the postions
        fixposition("port_horizontal_valve_left_" + str(i), xoffset, yoffset)
        yoffset = yoffset + 6000
        statement = "PORT port_horizontal_valve_right_" + str(i) + " r = 100; "
        writestatement(statement)

def printhorizontalcontrolchannels(grid_size, f):
    for y in range(1, grid_size+1):
        statement = "NET net_valve_horizontal_" + str(y) + " from " + "port_horizontal_valve_left_" + str(y) + " 2 to "
        for x in range(1, grid_size):
            statement = statement + " valve_horizontal_" + str(x) + "_"+ str(y) + " 3"
            #if x != grid_size - 1:
            statement = statement + ","
            statement = statement + " port_horizontal_valve_right_" + str(y) + " 4 channelWidth = 50; "
            writestatement(statement)


def printverticalvalveports(grid_size, f):
    for y in range(1, grid_size):
        statement = "PORT port_vertical_valve_left_" + str(y) + " r = 100; "
        writestatement(statement)
        statement = "PORT port_vertical_valve_right_" + str(y) + " r = 100; "
        writestatement(statement)

def printverticalcontrolchannels(grid_size, f):
    for y in range(1, grid_size):
        src = "port_vertical_valve_left_" + str(y)
        tar = "valve_vertical_" + str(1) + "_" + str(y)
        printchannel(src, 2, tar , 4, 50)
        for x in range(1, grid_size):
            src = "valve_vertical_" + str(x) + "_" + str(y)
            tar = "valve_vertical_" + str(x+1) + "_" + str(y)
            printchannel(src, 2, tar , 4, 50)
        src = "valve_vertical_" + str(grid_size) + "_" + str(y)
        tar = "port_vertical_valve_right_" + str(y)
        printchannel(src, 2, tar , 4, 50)

grid_size = input("Enter Grid Size: ")
grid_size = int(grid_size)
device_name = "xgrid_" + str(grid_size)
f = open(device_name + ".uf", 'w')

f.write("DEVICE " + device_name )
newline(f)
f.write("LAYER FLOW")
newline(f)

f.write("# Printing all the ports")
newline(f)

printtopports(grid_size, f)

printrightports(grid_size, f)

printbottomports(grid_size, f)

printleftports(grid_size, f)

printcelltraps(grid_size, f)

printinsidechannels(grid_size, f)

printoutsidechannels(grid_size, f)

f.write("END LAYER")
newline(f)

f.write("LAYER CONTROL")
newline(f)

printvalves(grid_size, f)

printverticalvalveports(grid_size, f)

printverticalcontrolchannels(grid_size, f)

printhorizontalvalveports(grid_size, f)

#printhorizontalcontrolchannels(grid_size, f)


f.write("END LAYER")
newline(f)
