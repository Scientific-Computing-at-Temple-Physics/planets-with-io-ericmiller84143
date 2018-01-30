# This is a comment.  Python will ignore these lines (starting with #) when running

import math as ma

float density
float radius


mass = input("What is the mass of the explorer? :")
alt = input("What is the altitude of the explorer? :")
name = raw_input("What is the planet of interest? :")

infile = open("planet_data.dat", "r")

for line in infile:  #loop over each line in the code
  temp = line.split(;)  #delimiter is the ; 
  if temp[0] == name:   #if the first element of the line matches the name user wants
    radius = temp[1]/1000   #set radius to the planet radius
    density = temp[2]*1000      #set density to the planet density
    break                   #stop looping because the planet and respective data was found
 

accel = (4/3)*ma.pi*6.674*(10**(-11))*radius*density

print "The explorer's weight is", accel*mass, "N"
