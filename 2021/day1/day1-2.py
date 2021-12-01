file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day1/input-day1.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day1/input-day1-test.txt"

f = open(file, "r")
data = f.readlines()

sum = 0
prevSum = 0
counter = 0

for idx, val in enumerate(data):
    if idx > 1:
        prevSum = sum
        sum = int(data[idx].strip()) + int(data[idx-1].strip()) + int(data[idx-2].strip())
        print(sum)
        
        if sum > prevSum and prevSum != 0:
            counter = counter + 1

print('counter: ' + str(counter))
print('Done.')