input = open('.\Day 2 Input' ,'r')

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

gameID_SUM = 0

for line in input:

    gameID, gameDATA = line.split(':')

    gameID = int(gameID.strip('Game').strip())
    gameDATA = gameDATA.replace(';', ',').split(',')

    validGame = True

    for set in gameDATA:

        count, color = set.split()
        count = int(count)

        match color:
            case 'red':
                if count > MAX_RED:
                    validGame = False
            case 'green':
                if count > MAX_GREEN:
                    validGame = False
            case 'blue':
                if count > MAX_BLUE:
                    validGame = False

    if validGame:
        gameID_SUM += gameID

print(gameID_SUM)