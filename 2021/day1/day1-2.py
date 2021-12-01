file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day1/input-day1.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day1/input-day1-test.txt"

f = open(file, "r")

depthOne = 0
depthTwo = 0 
depthThree = 0

depthSum = 0
previousDepthSum = 0

lineCount = 0
counter = 0

for x in f:
    newDepth = int(x.strip())
    lineCount = lineCount+1
    mod = lineCount % 3

    if mod == 1:
        depthOne = newDepth
    elif mod == 2:
        depthTwo = newDepth
    elif mod == 0:
        depthThree = newDepth

    if lineCount > 2:
        previousDepthSum = depthSum
        depthSum = depthOne + depthTwo + depthThree

        if depthSum > previousDepthSum and previousDepthSum != 0:
            counter = counter+1

    #print(str(lineCount))

print(str(counter))

print('Done.')