#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # declare a dictionary
    # iterate through entire array
    # add new key to dictionary or increment
    # any time the increment value is divisible by 2 add to total matches
    matches = {}
    total = 0

    for i in range(0, len(ar)):
        cur = ar[i]
        if not cur in matches.keys():
            matches[cur] = 1
        else:
            matches[cur] += 1
        if matches[cur] %2 is 0:
            total += 1

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
