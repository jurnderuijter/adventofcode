#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day9/input-day9-test.txt"
file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day9/input-day9.txt"

data = []

def setup():
    f = open(file, "r")
    data = f.readlines()   
    do(data) 

def do(data):
    grid = []
    sum = 0

    for line in data:
        line = line.strip()
        grid.append(list(line))

    print(grid)

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
                print(pos)
                sum += (int(pos)+1)

    print(str(sum))

setup()

print('Done.')
