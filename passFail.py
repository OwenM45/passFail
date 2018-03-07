#open file
inputFile = open("DATA11.txt","r")
#add DATA10 to an array
data = inputFile.readlines()

#the lines that the next weights and cloass size will be on
weightsLn = 0
stuNumLn = 1
#keeps track of the current line
counter = 0
#keeps track of the amount of passes per class
passes = 0
#saves the weights to use in the mark
weights = 0

#go through each line of DATA10
for line in data:
    #checks if this is a weight line
    if counter == weightsLn:
        #sets the weights
        weights = line.split()
        #prints the ammount of passes
        if passes != 0: print(passes)
        #resets passes variable
        passes = 0
    #checks if its a class size line
    elif len(line.split()) == 1:
        #sets the next weights line
        weightsLn += int(line)+2
    #checks if its a line with marks
    else:
        #sets the final grade variable
        final = 0
        #goes through the marks and weights 
        for weight, mark in zip(weights, line.split()):
            #calculates average
            final += int(weight)*int(mark)/100
        #checks if current student passed
        if final > 50: passes += 1
    #adds one to the counter
    counter += 1
print(passes)
#closes the file
inputFile.close
    
