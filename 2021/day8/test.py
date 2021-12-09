def isMatch(chars, string):
    goal = len(chars)
    count = 0
    for char in chars:
        if char in string:
            count += 1

    return goal == count


print(isMatch('gh','abcdefghij'))