# Eric Miller
#1-30-2018
#This file takes information from file: planet_data.dat. Given a mass and altitiude of an explorer on a specified planet, it returns 
# the weight and graviational acceleration of that explorer.

import math as ma

density = 0.0
radius =0.0
G=6.674*(10**(-11))

mass = input("What is the mass of the explorer? :")
alt = input("What is the altitude of the explorer? :")
name = raw_input("What is the planet of interest? :")

infile = open("planet_data.dat", "r")

for line in infile:  #loop over each line in the code
  temp = line.split(;)  #delimiter is the ;, split each line like this
  if temp[0] == name:   #if the first element of the line matches the name the user specified
    radius = temp[1]*1000   #set radius to the planet radius
    density = temp[2]*1000      #set density to the planet density
    break                   #stop looping because the planet and respective data was found
 

accel = (4/3)*(ma.pi)*G*radius*density

print "The explorer's weight is", accel*mass, "N. The gravitational acceleration is", accel/9.8 , "g's"

infile.close()
