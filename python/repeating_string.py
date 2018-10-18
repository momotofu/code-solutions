#!/bin/python3
import os


def countAsIn(s, n):
    if len(s) == 1:
        if s == 'a':
            return n
        else:
            return 0

    occurances = s.count('a')
    divisions = n // len(s)
    sub_total = occurances * divisions
    remainder = s[:n % len(s)].count('a')

    return sub_total + remainder


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s, n = input(), int(input())

    result = countAsIn(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
