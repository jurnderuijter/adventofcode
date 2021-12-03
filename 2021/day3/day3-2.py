file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day3/input-day3.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day3/input-day3-test.txt"

f = open(file, "r")
data = f.readlines()

def doCalc(data, mode):
    tempListOld = data
    tempListNew = []

    size = len(data[0].strip())

    for currPos in range(size):
        tempListNew = []

        #print(currPos)
        countZero = 0
        countOne = 0

        for val1 in tempListOld:
            val1 = val1.strip()
            #print(val1)

            if val1[currPos] == '0':
                countZero = countZero +1
            elif val1[currPos] == '1':
                countOne = countOne +1

        for val2 in tempListOld: 
            val2 = val2.strip()
            if mode == 1:
                if countZero > countOne and val2[currPos] == '0':
                    tempListNew.append(val2)
                if countZero <= countOne and val2[currPos] == '1':
                    tempListNew.append(val2)
            else:
                if countZero <= countOne and val2[currPos] == '0':
                    tempListNew.append(val2)
                if countZero > countOne and val2[currPos] == '1':
                    tempListNew.append(val2)

        tempListOld = tempListNew

        if len(tempListOld) == 1:
            break

    return str(tempListOld[0])

solution1 = doCalc(data, 1)
solution2 = doCalc(data, 2)

print(int(solution1,2) * int(solution2,2))

print('Done.')