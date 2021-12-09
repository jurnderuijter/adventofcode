#file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day8/input-day8-test.txt"
file = "/Users/jurnderuijter/projects/AdventOfCode/2021/day8/input-day8.txt"

data = []

def setup():
    f = open(file, "r")
    data = f.readlines()   
    do(data) 

def do(data):
    sum = 0
    for line in data:
        line = line.strip()
        #print(line)

        zero = ''
        one = ''
        two = ''
        three = ''
        four = ''
        five = ''
        six = ''
        seven = ''
        eight = ''
        nine = ''

        pattern = line.split(' | ')
        digits = sortArr(pattern[0].split(' '))
        parts = sortArr(pattern[1].split(' '))

        #print('{} | {}'.format(digits, parts))

        for digit in digits:
            # 1
            if len(digit) == 2:
                one = digit
            # 7               
            elif len(digit) == 3:
                seven = digit
            # 4
            elif len(digit) == 4:
                four = digit                 
            # 8
            elif len(digit) == 7:
                eight = digit

        for digit in digits:                                           
            # 0,6,9
            if len(digit) == 6:
                if isMatch(four,digit):
                    nine = digit
                elif isMatch(seven,digit) and isMatch(one,digit):
                    zero = digit
                else:
                    six = digit

        for digit in digits:             
            # 2,3,5
            if len(digit) == 5:
                if isMatch(seven,digit) and isMatch(one,digit):
                    three = digit
                elif isMatch(digit,nine):
                    five = digit
                else:
                    two = digit        

        # print('zero: ' + zero)
        # print('one: ' + one)     
        # print('two: ' + two)     
        # print('three: ' + three)     
        # print('four: ' + four)     
        # print('five: ' + five)     
        # print('six: ' + six)     
        # print('seven: ' + seven)     
        # print('eight: ' + eight)     
        # print('nine: ' + nine)
        
        outcome = ''

        for part in parts:
            if part == zero:
                outcome = outcome + '0'
            elif part == one:
                outcome = outcome + '1'                 
            elif part == two:
                outcome = outcome + '2'   
            elif part == three:
                outcome = outcome + '3'   
            elif part == four:
                outcome = outcome + '4'   
            elif part == five:
                outcome = outcome + '5'   
            elif part == six:
                outcome = outcome + '6'   
            elif part == seven:
                outcome = outcome + '7'   
            elif part == eight:
                outcome = outcome + '8'   
            elif part == nine:
                outcome = outcome + '9' 

        print('outcome: ' + outcome) 
        sum += int(outcome)
    
    print(sum)

def sortArr(arr):
    for (idx, val) in enumerate(arr):
        arr[idx] = "". join(sorted(val))
    return arr

def isMatch(chars, string):
    #print('check if {} is in {}'.format(chars, string))
    goal = len(chars)
    count = 0
    for char in chars:
        if char in string:
            count += 1

    return goal == count

setup()

print('Done.')