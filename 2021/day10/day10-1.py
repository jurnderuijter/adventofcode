#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day10/input-day10-test.txt"
file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day10/input-day10.txt"

data = []
patterns = ['{}','[]','()','<>']
sumCorrupted = 0

def setup():
    f = open(file, "r")
    data = f.readlines()   
    do(data) 

def replace(orgLine):
    line = orgLine
    for pat in patterns:
        line = line.replace(pat, '')

    if line != orgLine: 
        line = replace(line)
    return line

def do(data):
    global sumCorrupted
    for idx, line in enumerate(data):
        line = line.strip()
        print(idx)
        line = replace(line)
        print(line)

        for char in line:
            if '}' in char:
                sumCorrupted += 1197
                break
            elif ']' in char:
                sumCorrupted += 57
                break
            elif ')' in char:
                sumCorrupted += 3
                break
            elif '>' in char:
                sumCorrupted += 25137
                break

    print(sumCorrupted)

setup()

print('Done.')