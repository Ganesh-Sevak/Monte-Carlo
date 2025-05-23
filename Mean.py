import matplotlib.pyplot as plt
import numpy as np
import math
import random


lower = int(input("Enter the lower bound of your sample:\n"))
upper = int(input("Enter the upper bound of the sample:\n"))
trial = int(input("Sample size:\n"))

PopMean = float((upper+lower)/(2)) #this is the true population mean

#intialize the empty arrays for the x and y axis
AxisX = []
AxisY = []
temp = []
Truth = []

#populate the arrays
for i in range(1,trial+1,1):
    
    AxisX.append(i) #populates AxisX with incrementing numbers

    Truth.append(PopMean)
   
    temp.append(random.randint(lower,upper)) #Populating the temp array with a random number in range
    
    runSum = 0
    for j in range(len(temp)): #for every element of the temp array
        runSum+=temp[j] #this created the total for the array

    AxisY.append((runSum/i))
        

#Create the line graph
plt.plot(AxisX, AxisY, label = "Experiment Mean", color = 'red')
plt.plot(AxisX, Truth, label = "Exepcted Mean", color = 'black')

# Step 3: Add labels and title
plt.title("Law Of Large Numbers")
plt.xlabel("Trials:")
plt.ylabel("Mean")

#  Show the graph window
plt.legend()
plt.show()



