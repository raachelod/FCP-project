# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:48:09 2021

@author: fjmin
"""

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
    Is.write("\n" + days + "," +percentinfects )
    
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
    Is.write("\n"+days + "," + percentinfectss)
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
    Rs.write("\n" + days + "," +percentinfects )

while day<timeframe:
    day=day+1
    days=str(day)
    Rs.write("\n" + days + "," + percentinfects)

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
    Ss.write("\n" + days + "," + suss)
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
            Ss.write("\n" + days + "," + suss)
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
    Ss.write("\n" + days + "," + suss)
    
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
    Ss.write("\n" + days + "," + suss)

Ss.close()








