# Eric Miller
#1-30-2018
#This file takes information from file: planet_data.dat. Given a mass and altitiude of an explorer on a specified planet, it returns 
# the weight and graviational acceleration of that explorer.

import math as ma
G=6.674*(10**(-11))

mass = input("What is the mass (in kg) of the explorer? :")
alt = input("What is the altitude (in km) of the explorer above the planet? :")
name = raw_input("What is the planet of interest? :")

infile = open("planet_data.dat", "r")

for line in infile:  #loop over each line in the code
  temp = line.split(";")  #delimiter is the ;, split each line like this
  if temp[0].upper() == name.upper():   #if the first element of the line matches the planet the user specified
    temp2 = temp[1].split()     #split the radius portion (temp[1]) into number and units
    temp3 = temp[2].split()     #split the density portion (temp[2]) into number and units
    radius = float(temp2[0])   #set radius to the planet radius (in km)
    density = float(temp3[0])*1000     #set density to the planet density (in SI)
    break                   #stop looping because the planet and respective data was found
 

accel = (4.0/3)*(ma.pi)*G*(radius**3)*density/((alt+radius)**2)*1000

weight = round(accel * mass, 3)
gs = round(accel / 9.80665, 3)

print "The explorer's weight is", weight, "N. The gravitational acceleration is", gs , "g's"

infile.close()
