file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day1/input-day1.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day1/input-day1-test.txt"

f = open(file, "r")

depth = 0
counter = 0

for x in f:
    newDepth = int(x.strip())

    if newDepth > depth and depth != 0:
        counter = counter +1

    depth = newDepth

print(str(counter))

print('Done.')