input = open('.\Day 2 Input' ,'r')

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

powerSum = 0

for line in input:

    gameID, gameDATA = line.split(':')

    gameID = int(gameID.strip('Game').strip())
    gameDATA = gameDATA.replace(';', ',').split(',')

    redCounter, greenCounter, blueCounter = 0,0,0

    for set in gameDATA:

        count, color = set.split()
        count = int(count)

        match color:
            case 'red':
                if count > redCounter:
                    redCounter = count
            case 'green':
                if count > greenCounter:
                    greenCounter = count
            case 'blue':
                if count > blueCounter:
                    blueCounter = count

    powerSum += redCounter*greenCounter*blueCounter

print(powerSum)