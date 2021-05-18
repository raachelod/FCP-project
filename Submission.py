# -*- coding: utf-8 -*-
"""
Created on Mon May 17 16:23:43 2021

@author: pk20813, vk19682, tt20973, yh20989
"""
#Written by Finn

PopDen=int(input("please give a value for Population Density between 1 and 10000= "))
while PopDen>10000:
    print("please enter a value between 1 and 10000")
    PopDen=int(input("please give a value for Population Density between 1 and 10000= "))
while PopDen<1:
    print("please enter a value between 1 and 10000")
    PopDen=int(input("please give a value for Population Density between 1 and 10000= "))


MaxPercentageinfected=100*(0.0133*PopDen**0.2325)

Infectspread=int(input("Each infected person will come into contact and spread the virus to a certain amount of people during their infectios period, please give a value for how many people each infected person will infect before recovery= "))
while Infectspread<1:
    print("An infected individual can not cure others of the virus.")
    Infectspread=int(input("please give the value for how many people an individual will spread the virus to="))
InfectTime=int(input("Each infected person will only be infectious and able to spread the virus for a limited amount of time before they recover, please give a value for the number of days each person remains infectious for="))
while InfectTime<1:
    print("The virus spreads with time flowing linearly")
    InfectTime=int(input("please provide a value for how many days an individual will remain infectious for="))

timeframe=31
poptotal=1000000
Minperc=1/1000000
#infected
Is=open("infectionstats.txt","w")

prevday=1
currentcase=prevday+prevday*Infectspread
percentinfect=currentcase*100/poptotal 

day=0

while percentinfect<MaxPercentageinfected:
    currentcase=prevday*Infectspread+prevday
    prevday=currentcase
    percentinfect=currentcase*100/poptotal
    currentcases=str(currentcase)
    percentinfects=str(percentinfect)
    day=day+1
    days=str(day)
    Is.write(days + "," +percentinfects + "\n" )
    
recovery=1

while percentinfect>Minperc:
    lastday=currentcase
    recovered=recovery*Infectspread+recovery
    recovery=recovered
    currentcase=lastday-recovery
    if currentcase<0:
        currentcase=0
    percentinfect=currentcase*100/poptotal
    recoverds=str(recovered)
    percentinfectss=str(percentinfect)
    day=day+1
    days=str(day)
    Is.write(days + "," + percentinfectss + "\n")
Is.close()


#recoverd
day=InfectTime
prevday=1
Rs=open("recoverystats.txt","w")

while percentinfect<MaxPercentageinfected:
    currentcase=prevday*Infectspread+prevday
    prevday=currentcase
    percentinfect=currentcase*100/poptotal
    currentcases=str(currentcase)
    percentinfects=str(percentinfect)
    day=day+1
    days=str(day)
    Rs.write(days + "," +percentinfects + "\n" )

while day<timeframe:
    day=day+1
    days=str(day)
    Rs.write(days + "," + percentinfects + "\n")

Rs.close()

#susceptible
prevday=1
recday=1
recovery=1
currentcase=prevday+prevday*Infectspread
percentinfect=currentcase*100/poptotal 
day=0
Ss=open("susceptiblestats.txt","w")

while percentinfect<MaxPercentageinfected:
    currentcase=prevday*Infectspread+prevday
    prevday=currentcase
    percentinfect=currentcase*100/poptotal
    sus=100-percentinfect
    suss=str(sus)
    day=day+1
    days=str(day)
    Ss.write(days + "," + suss + "\n")
    if day>InfectTime:
        while percentinfect<MaxPercentageinfected:
            currentcase=prevday*Infectspread+prevday
            prevday=currentcase
            percentinfect=currentcase*100/poptotal
            currentrec=recday*Infectspread+recday
            recday=currentrec
            percentrec=currentrec*100/poptotal
            nonsus=percentinfect+percentrec
            sus=100-nonsus
            suss=str(sus)
            day=day+1
            days=str(day)
            Ss.write(days + "," + suss + "\n")
while percentrec<MaxPercentageinfected:
    currentrec=recday*Infectspread+recday
    recday=currentrec
    percentrec=currentrec*100/poptotal
    lastday=currentcase
    recovered=recovery*Infectspread+recovery
    recovery=recovered
    currentcase=lastday-recovery
    percentinfect=currentcase*100/poptotal
    nonsus=percentinfect+percentrec
    sus=100-nonsus
    suss=str(sus)
    day=day+1
    days=str(day)
    Ss.write(days + "," + suss + "\n")
    
while day<timeframe:
    lastday=currentcase
    recovered=recovery*Infectspread+recovery
    recovery=recovered
    currentcase=lastday-recovery
    if currentcase<0:
        currentcase=0
    percentinfect=currentcase*100/poptotal
    nonsus=percentinfect+percentrec
    sus=100-nonsus
    suss=str(sus)
    day=day+1
    days=str(day)
    Ss.write(days + "," + suss + "\n")

Ss.close()

#Written by Chris

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
    
    file = open("infectionstats.txt", "r")  # reads the file 
    
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
    
    file2 = open("recoverystats.txt", "r") # open the recovery text file
    
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
    
    file3 = open("susceptiblestats.txt", "r")
    
    x2_data = []
    y2_data = [] # this is for percentage of people

    for line in file3:
        i = line.split(',')
        values = [float(s) for s in i]
        x2_data.append( values[0] )
        y2_data.append( values[1] )
    plt.plot(x2_data, y2_data, color = "k", label = "Susceptible")
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

#Written by Huangmo & Rachel

from matplotlib import pyplot as plt 
import csv
from math import pow
import numpy as np
import os
if not os.path.exists('images'):
    os.makedirs('images')

np.random.seed(100)

DAYS = 200

INFECT_X = 10

def cal_infect_percentage(density):
    return 0.0133 * pow(density, 0.2325)


class Simulation:
    def __init__(self, name, population, population_density, days):
    
        self.name = name
        
        self.population = population
        
        self.population_density = population_density

        
        self.popsize = int(self.population_density)
       
    
        self.days = days

        
        self.infect_precentage = cal_infect_percentage(self.population_density)

        
        self.incubation = [0] * self.days
        
        self.infected_person  = [1] * self.days
        
        self.susceptible_person = [self.popsize - self.infected_person[0]] * self.days


    def run(self):
        
        for x in range(self.days - 1):
            
            incubation = INFECT_X*self.infect_precentage*self.susceptible_person[x]*self.infected_person[x]/self.popsize
            
            self.susceptible_person[x + 1] = self.susceptible_person[x] - incubation
            self.incubation[x + 1] = self.incubation[x+1] + incubation
            if x > 15:
                
                self.infected_person[x + 1] = self.infected_person[x] + self.incubation[x-15]
                self.incubation[x] -= self.incubation[x-15]
            else:
                
                self.infected_person[x + 1] = self.infected_person[x]
        
        plt.title("simlation demo: {}".format(self.name)) 
        plt.xlabel("Day") 
        plt.ylabel("Person Count") 
        plt.plot(self.susceptible_person, label="susceptible")
        plt.plot(self.incubation, label="incubation")
        plt.plot(self.infected_person, label="infected")
        plt.legend()
        plt.savefig('images/{}.png'.format(self.name), format='png')


def main():
    with open('population.csv')as f:
        f_csv = csv.reader(f)
        
        next(f_csv)
        
        for row in f_csv:
            name = row[0]
            population = int(row[3].replace('"','').replace(',',''))
            density = float(row[4].replace('"','').replace(',',''))
            print(name, population, density)
            sim = Simulation(name, population, density, DAYS)
            sim.run()
            
            break

if __name__ == "__main__":
    main()
class Animation:
    "Create animation of epidemic"
    
    def __init__(self, simulation, duration):
        self.simulation = simulation
        self.duration = duration
        
        self.figure = plt.figure(figsize=(5,5))
        self.axes_grid = self.figure.add
     
        
    def show(self):
        "Run the animation on the screen"
        animation = FuncAnimation(self.figure, self.update, frames = range(100), init_func = self.init, blit=True, interval=200)
        plt.show()
    
    def init(self):
        actors = []
        actors += self.gridanimation.init()
        return actors
    
    def update(self, framenumber):
        self.simulation.update()
        actors = []
        actors += self.gridanimation.update(framenumber)
        return actors 

