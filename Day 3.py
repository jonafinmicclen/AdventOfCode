import numpy as np
input = open('.\Day 3 Input' ,'r')

nonSymbols = ['1','2','3','4','5','6','7','8','9','0','.']
symbols = []

#Load file into array
inputArray = []
for line in input:
    temp = []
    for char in line.strip():
        
        if char not in nonSymbols: #Get list of symbols
            symbols.append(char)
            
        temp.append(char)
    inputArray.append(temp)

inputArray = np.array(inputArray)
SYMBOLS = set(symbols)
height, width = inputArray.shape
isNumber = False
isValid = False
currentNumber = ''
symbolsDetected = []
totalSum =  0

for x in range (width):
    for y in range(height):
        
        if str(inputArray[x,y]).isnumeric(): 
            
            isNumber = True
            currentNumber += inputArray[x,y]

            for xOffset in range(-1,2): #Faster method by checking on grid and adding 2 rows and columns of '.'
                for yOffset in range(-1,2):
                    
                    #if in range of grid check if its symbol
                    if 0 <= x+xOffset < inputArray.shape[0] and 0 <= y+yOffset < inputArray.shape[1] and inputArray[x+xOffset,y+yOffset] in SYMBOLS:
                        isValid = True
                        symbolsDetected.append(inputArray[x+xOffset,y+yOffset])

        else:

            if isNumber and isValid:
                totalSum += int(currentNumber)
                print('valid', currentNumber,set(symbolsDetected))
            
            #if isNumber and not isValid:
                #print('invalid ',currentNumber)
                
            currentNumber = ''
            symbolsDetected = []
            isNumber = False
            isValid = False
            
print(f'The sum of all of the part numbers in the engine schematic is {totalSum}.')
print(inputArray)