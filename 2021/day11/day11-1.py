file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day11/input-day11-test.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day11/input-day11-test2.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day11/input-day11.txt"

data = []
grid  = []
steps = 10

def setup():
    f = open(file, "r")
    data = f.readlines()   
    do(data) 

def printGrid():
    global grid
    print('----------')  
    for row in grid:
        printRow = ''
        for col in row:
            printRow = printRow + str(col)
        print(printRow)
    print('----------')  

def flash(x, y):
    global grid

    colPrint = str(x) + ':' + str(y)
    print(colPrint)
    col = grid[x][y]

    if col != 'F':
        col = int(col) + 1
        grid[x][y] = col
        
        if int(col) > 9:
            # go flash
            print('flash: ' + colPrint)
            col = 'F'
            grid[x][y] = col

            maxRow = len(grid)-1
            #print('maxRow: ' + str(maxRow))
            maxCol = len(grid[x])-1
            #print('maxCol: ' + str(maxCol))
                
            # rows
            if (x!= 0):
                #print('top row')
                flash(x-1, y)

                # diag
                if y != 0:
                    #print('left diag - top row down')
                    flash(x-1, y-1)
                if y != maxCol:
                    #print('right diag - top row down')
                    flash(x-1, y+1)

            elif (x != maxRow):
                #print('bottom row')
                flash(x+1, y)

                # diag
                if y != 0:
                    #print('left diag - bottom row up')
                    flash(x+1, y-1)
                if y != maxCol:
                    #print('right diag - bottom row up')
                    flash(x+1, y+1)

            else:
                #print('middle row down')
                flash(x+1, y)
                #print('middle row up')
                flash(x-1, y)

                # diag
                if y != 0:
                    #print('left diag - middle row down')
                    flash(x+1, y-1)
                    #print('left diag - middle row up')
                    flash(x-1, y-1)
                if y != maxCol:
                    #print('right diag - middle row down')
                    flash(x+1, y+1)
                    #print('right diag - middle row up')
                    flash(x-1, y+1)

            # cols
            if (y != 0):
                #print('left col')
                flash(x, y-1)
            elif (y != maxCol):
                #print('right col')
                flash(x, y+1)
            else:
                #print('middle col')
                flash(x, y-1)
                flash(x, y+1)
                        

def do(data):
    global grid
    global steps

    for line in data:
        line = line.strip()
        grid.append(list(line))

    printGrid()
    
    # increase energy lvls by steps
    for step in range(steps):
        for idx, row in enumerate(grid):
            for idy, col in enumerate(row):
                grid[idx][idy] = int(grid[idx][idy])+1

        for idx, row in enumerate(grid):
            for idy, col in enumerate(row):
                if col != 'F' and int(col) > 9:
                    flash(idx, idy)

        for idx, row in enumerate(grid):
            for idy, col in enumerate(row):
                if col == 'F':
                    #grid[idx][idy] = 0
                    print()

        printGrid()

setup()

print('Done.')