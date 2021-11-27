file = "/Users/jurnderuijter/projects/AdventOfCode/2020/day3/input-day3.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2020/day3/input-day3-test.txt"

f = open(file, "r")

position = 0
numOfTrees = 0
numOfNone = 0
lineNr = 0

for x in f:
    x = x.strip()
    if lineNr > 0:
        #print(x)
        # set line length first time
        maxLen = len(x)
        #print('maxLen: ' + str(maxLen)) 
        position = position + 3 
        #print('position: ' + str(position))
        remainder = position % maxLen
        #print('remainder: ' + str(remainder))

        charAtPos = x[remainder]
        #print('char at position: ' + charAtPos)

        if charAtPos == '#':
            numOfTrees = numOfTrees +1
        elif charAtPos == '.':
            numOfNone = numOfNone +1

    lineNr = lineNr+1

print('numOfTrees: ' + str(numOfTrees))
print('numOfNone: ' + str(numOfNone))

print('Done.')