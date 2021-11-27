file = "/Users/jurnderuijter/projects/AdventOfCode/2020/day3/input-day3.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2020/day3/input-day3-test.txt"

def stepSlope(stepRight, stepDown):
    currentLine = 0
    targetLine = stepDown

    position = 0
    numOfTrees = 0
    numOfNone = 0

    f = open(file, "r")

    for x in f:
        x = x.strip()

        if currentLine == targetLine:
            #print(x)
            # set line length first time
            maxLen = len(x)
            #print('maxLen: ' + str(maxLen)) 
            position = position + stepRight
            #print('position: ' + str(position))
            remainder = position % maxLen
            #print('remainder: ' + str(remainder))

            charAtPos = x[remainder]
            #print('char at position: ' + charAtPos)

            if charAtPos == '#':
                numOfTrees = numOfTrees +1
            elif charAtPos == '.':
                numOfNone = numOfNone +1

            targetLine = currentLine + stepDown

        currentLine = currentLine + 1

    #print('numOfTrees: ' + str(numOfTrees))
    #print('numOfNone: ' + str(numOfNone))

    return numOfTrees

print(stepSlope(1,1) * stepSlope(3,1) * stepSlope(5,1) * stepSlope(7,1) * stepSlope(1,2))

print('Done.')