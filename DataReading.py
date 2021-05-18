# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:59:04 2021

@author: colin
"""

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight') 

fig, ax = plt.subplots()
ax.set_xlim(0,30)  #setting limit in x axis
ax.set_ylim(0,100)
#line, = ax.plot(0,0)

plt.xlabel("Days")
plt.ylabel("Population density Percentage")

#________________________________________________-

def plotInf(i): #Infected
    
    file = open("DataInf.txt", "r")  # reads the file 
    
    x_data = [] # this is for the days
    y_data = []
    
    for line in file:
        a = line.split(',')
        values = [float(s) for s in a]
        x_data.append( values[0] )
        y_data.append( values[1] )           
    #fig, ax.clear()
    plt.plot(x_data, y_data, color = "red", label = "Infected")   
    plt.legend()
    return
    
#___________________________________________________________

def plotRec(i):  #Recovery
    
    file2 = open("DataRec.txt", "r") # open the recovery text file
    
    #create a list for the x and y values for the days and the % of people recovering
    x1_data = [] # this is for the days
    y1_data = [] # this is for percentage of people

    for line in file2:
        i = line.split(',')
        values = [float(s) for s in i]
        x1_data.append( values[0] )
        y1_data.append( values[1] )
    plt.plot(x1_data, y1_data, color = "green", label = "Recovery")
    plt.legend()                
    return

#________________________________________________________________________

def plotSus(i):
    
    file2 = open("DataSus.txt", "r")
    
    x2_data = []
    y2_data = [] # this is for percentage of people

    for line in file2:
        i = line.split(',')
        values = [float(s) for s in i]
        x2_data.append( values[0] )
        y2_data.append( values[1] )
    plt.plot(x2_data, y2_data, color = "k", label = "Recovery")
    plt.legend()                
    return


def updateALL(i):
    a = plotInf(i)
    b = plotRec(i)
    c = plotSus(i)
    return a+b+c

animALL = FuncAnimation(fig, updateALL,
                        interval = 20, blit = True)

plt.show()






