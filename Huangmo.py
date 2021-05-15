# coding:utf-8
"""
"""

from matplotlib import pyplot as plt 
from matoplotlib.animation import FuncAnimation
import csv
from math import pow
import random
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
