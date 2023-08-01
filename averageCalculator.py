def calculateAverage(scores):
    sumlist=0
    for i in range(len(scores)):
        sumlist +=scores[i]
        average = sumlist /(len(scores))
    return average
values = []
print("Please enter values you want to calculte average, C to confirm:")
userInput = input("")
while userInput.upper() != "C" :
    values.append(float(userInput))
    userInput = input("")
    
print("Your list of scores: ",values)
   
print("The average is: ",calculateAverage(values))

