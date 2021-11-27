f = open("/Users/jurnderuijter/projects/AdventOfCode/2020/day2/input-day2-1.txt", "r")

total = 0

for x in f:
  #print(x)

  pos = x.find("-")
  min = x[0:pos]

  pos2 = x.find(" ")
  max = x[(pos+1):pos2]

  pos3 = x.find(":")
  char = x[(pos2+1):pos3]
  pattern = x[(pos3+2):len(x)-1]
  
  # input = "{}-{} {}: {}".format(min, max, char, pattern)
  input = "{min}-{max} {char}: {pattern}".format(min = min, max = max, char = char, pattern = pattern)
  print(input)

  times = pattern.count(char)
  print(times)

  if int(min) <= times <= int(max):
      total = total+1

print(total)





