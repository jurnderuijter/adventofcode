#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day10/input-day10-test.txt"
file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day10/input-day10.txt"

data = []
patterns = ['{}','[]','()','<>']
corrChars = ']})>'

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
    scoreList = []
    for idx, line in enumerate(data):
        line = line.strip()
        line = replace(line)

        skip = False

        for cChar in corrChars:
            if cChar in line:
                skip = True

        if not skip:
            #print('{} : {}'.format(idx,line))

            score = 0
            completedLine = ''
            for c in reversed(line):
                if c == '(':
                    completedLine = completedLine + ')' 
                    score = (score * 5) + 1                 
                if c == '[':
                    completedLine = completedLine + ']'
                    score = (score * 5) + 2
                if c == '{':
                    completedLine = completedLine + '}'
                    score = (score * 5) + 3
                if c == '<':
                    completedLine = completedLine + '>'
                    score = (score * 5) + 4

            #print(completedLine)
            #print(score)
            scoreList.append(score)
            
    scoreList.sort()
    print(scoreList)
    mPos = int(len(scoreList) / 2)
    print(scoreList[mPos])


setup()

print('Done.')