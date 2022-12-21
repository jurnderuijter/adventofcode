import os
import sys


def main(file_name):
    calories = []
    i = 0

    with open(os.path.join(sys.path[0], file_name)) as infile:
        for line in infile:
            line = line.strip()

            if (line):
                if (len(calories) == i):
                    calories.append(int(line))
                else:
                    calories[i] += int(line)
            else:
                i += 1

    print(max(calories))


if __name__ == '__main__':
    file_name = 'input-real.txt'
    main(file_name)
