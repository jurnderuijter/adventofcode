#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day3/input-day3.txt"
file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day3/input-day3-test.txt"

f = open(file, "r")
data = f.readlines()

size = len(data[0].strip())
collection = []
for i in range(size):
    collection.append({'nul': 0, 'een': 0})

gamma = ''
epsilon = ''

for line in data:
    line = line.strip()
    #print(line)
    for idx, val in enumerate(line):
        #print('idx:{} - val:{}'.format(idx, val))
        entry = collection[idx]
        #print(entry)
        if val == '0':
            entry['nul'] = entry['nul'] + 1
            #print(collection[idx]['nul'])
        elif val == '1':
            entry['een'] = entry['een'] + 1
            #print(collection[idx]['een'])
        
        #print(collection[idx])
        #print(collection)


for entry in collection:
    if entry['nul'] > entry['een']:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
    else:
        gamma = gamma + '1'
        epsilon = epsilon + '0'

print(gamma)
print(epsilon)
print(int(gamma,2) * int(epsilon,2))
print('Done.')