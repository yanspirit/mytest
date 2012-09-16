#!/usr/local/bin/python

days  = 365
numPeople =23
prob = 0

while prob < 0.5:
    numPeople += 1
    prob = 1 -((1-prob)*(days-(numPeople-1))/days)
    print("Number of people:",numPeople)
    print("Prob. of same birthday:",prob)