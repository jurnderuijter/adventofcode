import numpy as np

#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day9/input-day9-test.txt"
file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day9/input-day9.txt"

data = []
basins = dict()

def setup():
    f = open(file, "r")
    data = f.readlines()   
    do(data) 

def check(currKey, grid, val, rowId, colId, rowMax, colMax):
    val = int(val)
    # top  
    if rowId != 0:
        pos = int(grid[rowId-1][colId])
        if pos > val and pos != 9:
            newPoint = '{}:{}={}'.format(rowId-1, colId, pos)

            if newPoint not in basins[currKey]:
                basins[currKey].append(newPoint)
                check(currKey, grid, pos, rowId-1, colId, rowMax, colMax)
    # bottom
    if rowId != rowMax-1:
        pos = int(grid[rowId+1][colId])
        if pos > val and pos != 9:
            newPoint = '{}:{}={}'.format(rowId+1, colId, pos)

            if newPoint not in basins[currKey]:
                basins[currKey].append(newPoint)
                check(currKey, grid, pos, rowId+1, colId, rowMax, colMax)
    # left
    if colId != 0:
        pos = int(grid[rowId][colId-1])
        if pos > val and pos != 9:
            newPoint = '{}:{}={}'.format(rowId, colId-1, pos)

            if newPoint not in basins[currKey]:
                basins[currKey].append(newPoint)
                check(currKey, grid, pos, rowId, colId-1, rowMax, colMax) 
    # right
    if colId != colMax-1:
        pos = int(grid[rowId][colId+1])
        if pos > val and pos != 9:
            newPoint = '{}:{}={}'.format(rowId, colId+1, pos)

            if newPoint not in basins[currKey]:
                basins[currKey].append(newPoint) 
                check(currKey, grid, pos, rowId, colId+1, rowMax, colMax)

def do(data):
    grid = []

    for line in data:
        line = line.strip()
        grid.append(list(line))

    #print(grid)

    for (rowId,row) in enumerate(grid):
        for (posId,pos) in enumerate(row):
            target = 0
            count = 0
            #print('{} (row: {} - pos: {})'.format(pos, rowId, posId))
            
            # vertical check
            if rowId == 0:
                target += 1
                #upper most row
                if (pos < grid[rowId+1][posId]):
                    count += 1
            elif rowId == len(grid)-1:
                target += 1
                #lower most row
                if (pos < grid[rowId-1][posId]):
                    count += 1
            else:
                target += 2
                #middle row
                if (pos < grid[rowId+1][posId]):
                    count += 1
                if (pos < grid[rowId-1][posId]):
                    count += 1                    

            # horizontal check
            if posId == 0:
                target += 1
                #left most pos
                if (pos < grid[rowId][posId+1]):
                    count += 1                
            elif posId == len(row)-1:
                target += 1
                #right most pos
                if (pos < grid[rowId][posId-1]):
                    count += 1                  
            else:
                target += 2
                #middle pos
                if (pos < grid[rowId][posId+1]):
                    count += 1
                if (pos < grid[rowId][posId-1]):
                    count += 1                   

            #print('target({}) == count({})'.format(str(target), str(count)))
            if (target == count):
                #print(pos)

                currKey = '{}:{}={}'.format(rowId, posId, pos)
                basins[currKey] = [currKey]
                check(currKey, grid, pos, rowId, posId, len(grid), len(row))

                #print(basins[currKey])

    basinSizes = []

    for key in basins:
        basinSizes.append(len(basins[key]))

    basinSizes.sort(reverse=True)
    print(basinSizes)

    print(basinSizes[0] * basinSizes[1] * basinSizes[2])

setup()

print('Done.')
