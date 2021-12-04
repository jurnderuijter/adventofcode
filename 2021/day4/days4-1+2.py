#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day4/input-day4-test.txt"
#bingoArr = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day4/input-day4.txt"
bingoArr = [13,47,64,52,60,69,80,85,57,1,2,6,30,81,86,40,27,26,97,77,70,92,43,94,8,78,3,88,93,17,55,49,32,59,51,28,33,41,83,67,11,91,53,36,96,7,34,79,98,72,39,56,31,75,82,62,99,66,29,58,9,50,54,12,45,68,4,46,38,21,24,18,44,48,16,61,19,0,90,35,65,37,73,20,22,89,42,23,15,87,74,10,71,25,14,76,84,5,63,95]

data = []
boards = []

def setup():
    print(setup)
    f = open(file, "r")
    data = f.readlines()    
    board = []
    lineCounter = 0

    for line in data:
        line = line.strip()
        
        if line != '':
            lineCounter = lineCounter+1
            #print(line)
            numbers = line.split(' ')
            #print(numbers)
            row = []
            for nr in numbers:
                if nr != '':
                    nrObj = {int(nr):''}
                    row.append(nrObj)
            board.append(row)

        if lineCounter == 5:
            boards.append(board)
            #print(board)
            board = []
            lineCounter = 0

    #print(boards)

def markBoards(nr):
    #print('BINGO nr = ' + str(nr))
    for board in boards:
        for row in board:
            for nrObj in row:
                key = int(list(nrObj.keys())[0])
                #print(key)
                if key == nr:
                    #print('match')
                    nrObj[key] = 'x'
                #print(nrObj)

    #print(boards)

def checkBingo():
    for board in boards:

        markedCol1 = 0
        markedCol2 = 0
        markedCol3 = 0
        markedCol4 = 0
        markedCol5 = 0

        for row in board:
            colCounter = 0
            markedCounter = 0
        
            for nrObj in row:
                colCounter = colCounter +1
                #print(row)
                #print(colCounter)

                if list(nrObj.values())[0] == 'x':
                    markedCounter = markedCounter+1

                    if colCounter == 1:
                        markedCol1 = markedCol1+1
                    elif colCounter == 2:
                        markedCol2 = markedCol2+1
                    elif colCounter == 3:
                        markedCol3 = markedCol3+1
                    elif colCounter == 4:
                        markedCol4 = markedCol4+1
                    elif colCounter == 5: 
                        markedCol5 = markedCol5+1  

                if markedCounter == 5 or markedCol1 == 5 or markedCol2 == 5 or markedCol3 == 5 or markedCol4 == 5 or markedCol5 == 5:
                    print('row: ' + str(markedCounter))
                    print('col1: ' + str(markedCol1))
                    print('col2: ' + str(markedCol2))
                    print('col3: ' + str(markedCol3))
                    print('col4: ' + str(markedCol4))
                    print('col5: ' + str(markedCol5))
                    print('BINGO!')
                    return board

        # check bingo in cols
    return False

def do():
    for nr in bingoArr:
        markBoards(nr)
        board = checkBingo()

        if board:
            calcScore(board, nr)
            return board

def calcScore(board, nr):
    print('calcScore')
    sum = 0

    for row in board:
        print(row)
        
        for nrObj in row:
            key = int(list(nrObj.keys())[0])
            if list(nrObj.values())[0] == '':
                sum = sum + int(key)
    
    #print(sum)
    print('solution: ' + str(sum * nr))

setup()
while len(boards) > 0:
    winningBoard = do()
    boards.remove(winningBoard)
    print(boards)

print('Done.')