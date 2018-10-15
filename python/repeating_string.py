#!/bin/python3

import os

def countOccurancesOfAIn(s, limit):
    total = 0

    for i in range(limit):
        if s[i] == 'a':
            total += 1
    return total


def repeatedString(s, n):
    length = len(s)
    total = 0

    total += countOccurancesOfAIn(s)

    if n > length:
        x = round(n / length, 1)
        times_divided = int(x)
        remaining_chars = int((x - int(x)) * 10)

    if times_divided > 1:
        total *= times_divided

    total += countOccurancesOfAIn(s, remaining_chars)

    return total







if __name__ == '__main__':
    fptr = open(os.inviron['OUTPUT_PATH'], 'w')

    s = input()
    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')
    fptr.close()
