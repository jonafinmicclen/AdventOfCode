import numpy as np
input = open('.\Day 3 Input' ,'r')

nonSymbols = ['1','2','3','4','5','6','7','8','9','0','.']
symbols = []

#Load file into array
inputArray = []
for line in input:
    temp = []
    for char in line.strip():
        
        if (char in nonSymbols) == False: #Get list of symbols
            symbols.append(char)
            
        temp.append(char)
    inputArray.append(temp)

inputArray = np.array(inputArray)
SYMBOLS = set(symbols)

height, width = inputArray.shape
isNumber = False
isValid = False
currentNumber = ''
totalSum =  0

print(SYMBOLS)
print(inputArray.shape)

for x in range (width):
    for y in range(height):

        if str(inputArray[x,y]).isnumeric(): 
            
            isNumber = True
            currentNumber += inputArray[x,y]

            for xOffset in range(-1+x,2+x): #Faster method by checking on grid and adding 2 rows and columns of '.'
                for yOffset in range(-1+y,2+y):

                    if 0 <= xOffset < inputArray.shape[0] and 0 <= yOffset < inputArray.shape[1] and inputArray[xOffset,yOffset] in SYMBOLS:
                            isValid = True

        else:

            if isNumber and isValid:
                totalSum += int(currentNumber)
                print(currentNumber, 'is valid')

            currentNumber = ''
            isNumber = False
            isValid = False
            
print(f'The sum of all of the part numbers in the engine schematic is {totalSum}.')