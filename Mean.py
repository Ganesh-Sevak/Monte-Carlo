import matplotlib.pyplot as plt
import math
import random




#Note: The names of the variables in main were not intentionally named the same as the variables
#in the getting inputs helper functions
#helper function to get the lower bound of the range
def get_lowerbound():
    while True: #Creates and infinte loop
        try:
            lower = int(input("Enter the lower bound of your sample:\n"))
            return lower #if its a valid input return the valid input
        except ValueError: #used to handle any charecter or string inputs
            print("Invalid input! Please enter a whole number.")
            return get_lowerbound() #if the input is invalid, return a valid one via asking again


#helper to get the upper bound of the range
def get_upperbound():
    while True:
        try:
            upper = int(input("Enter the upper bound of the sample:\n"))
            return upper
        except ValueError: #used to handle any charecter or string inputs
            print("Invalid input! Please enter a whole number.")
            return get_upperbound()

# helper to get the size of the "random" sample
def get_trials():
    while True:
        try:
            trial = int(input("Sample size:\n"))
            if trial <=0:
                print("Invalid input! Please enter a positive number.") 
                return get_trials()  
            return trial 

        except ValueError: #used to handle any charecter or string inputs
            print("Invalid input! Please enter a whole number.")    
            return get_trials()






def main():
    lower = get_lowerbound()
    upper = get_upperbound()
    trial = get_trials()
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
    plt.plot(AxisX, Truth, label = "Expected Mean", color = 'black')

    # Step 3: Add labels and title
    plt.title("Law Of Large Numbers")
    plt.xlabel("Trials:")
    plt.ylabel("Mean")

    #  Show the graph window
    plt.legend()
    plt.show()


#Starting the program
main()

