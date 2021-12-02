
file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day2/input-day2.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day2/input-day2-test.txt"

f = open(file, "r")
data = f.readlines()

x = 0
y = 0
aim = 0

for idx, val in enumerate(data):
    delim = val.find(" ")
    dir = val[0:(delim)]
    spaces = int(val[delim+1:len(val.strip())])

    input = "{}:{}".format(dir, spaces)
    #print(input)

    if dir == 'forward':
        x = x + spaces
        y = y + (aim * spaces)
    elif dir == 'down':
        aim = aim + spaces
    elif dir == 'up':
        aim = aim - spaces

print (x*y)
print('Done.')