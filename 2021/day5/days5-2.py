#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day5/input-day5-test.txt"
file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day5/input-day5.txt"

data = []

def setup():
    f = open(file, "r")
    data = f.readlines()   

    do(data) 

def do(data):
    grid = dict()

    for line in data:
        line = line.strip()
        #print(line)

        points = line.split(' -> ')
        start = points[0]
        end = points[1]
        x1 = int(start.split(',')[0])
        y1 = int(start.split(',')[1])
        x2 = int(end.split(',')[0])
        y2 = int(end.split(',')[1])

        #print('line: {},{} -> {},{}'.format(x1, y1, x2, y2))

        if (x1 == x2):
            for i in range(min(y1,y2), max(y1,y2)+1):
                location = '{},{}'.format(x1,i)
                grid[location] = grid.get(location, 0) + 1
        elif (y1 == y2):
            for i in range(min(x1,x2), max(x1,x2)+1):
                location = '{},{}'.format(i,y1)
                grid[location] = grid.get(location, 0) + 1
        else:
            if x1 > x2:
                xLocs = list(reversed(range(x2, x1+1)))
            else:
                xLocs = list(range(x1, x2+1))

            if y1 > y2:
                yLocs = list(reversed(range(y2, y1+1)))
            else:
                yLocs = list(range(y1, y2+1))

            for idx, val in enumerate(xLocs):
                location = '{},{}'.format(val,yLocs[idx])
                #print(location)
                grid[location] = grid.get(location, 0) + 1

    #print(grid)   

    overlaps = 0
    for pos, times in grid.items():
        if times > 1:
            overlaps += 1

    print(str(overlaps))

setup()

print('Done.')