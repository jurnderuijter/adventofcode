import os
import sys


def main(file_name):
    calories = []
    i = 0

    with open(os.path.join(sys.path[0], file_name)) as infile:
        for line in infile:
            line = line.strip()

            if (line):
                try:
                    calories[i] += int(line)
                except IndexError:
                    calories.append(int(line))
            else:
                i += 1

        print(max(calories))


if __name__ == '__main__':
    main('input-real.txt')
