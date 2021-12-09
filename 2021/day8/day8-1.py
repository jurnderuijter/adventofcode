file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day8/input-day8-test.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day8/input-day8.txt"

data = []

def setup():
    f = open(file, "r")
    data = f.readlines()   
    do(data) 

def do(data):
    count = 0
    for line in data:
        line = line.strip()
        print(line)

        pattern = line.split(' | ')
        parts = pattern[1].split(' ')

        # search for 2,3,4,7
        for part in parts:
            if (len(part) in (2,3,4,7)):
                count +=1
        print(parts)

    print(count)

setup()

print('Done.')
