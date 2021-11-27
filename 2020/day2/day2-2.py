file = "/Users/jurnderuijter/projects/AdventOfCode/2020/day2/input-day2.txt"
#file = "/Users/jurnderuijter/projects/AdventOfCode/2020/day2/input-day2-test.txt"

f = open(file, "r")

total = 0

for x in f:
  #print(x)

  pos = x.find("-")
  min = int(x[0:pos])

  pos2 = x.find(" ")
  max = int(x[(pos+1):pos2])

  pos3 = x.find(":")
  char = x[(pos2+1):pos3]
  pattern = x[(pos3+2):len(x)-1]
  
  # input = "{}-{} {}: {}".format(min, max, char, pattern)
  input = "{min}-{max} {char}: {pattern}".format(min = min, max = max, char = char, pattern = pattern)
  print(input)
  
  posMin = ''
  posMax = ''
  patternLen = len(pattern)

  print('length pattern: ' + str(patternLen))

  if min <= patternLen:
    posMin = pattern[(min-1)]
    print(posMin)
  
  if max <= patternLen:
    posMax = pattern[(max-1)]
    print(posMax)

  if (char == posMin and char != posMax) or (char != posMin and char == posMax):
    total = total+1

print(total)





