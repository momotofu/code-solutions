#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # Can only jump on clouds that are cumulus and that
    # have indices of current index + 1 or 2.
    # if a thunderhead is between a double jump.
    # so basically you can skip a cumulus but you cant
    # skip a thunderhead
    curIndex = 0
    numberOfJumps = 0

    while curIndex < len(c) - 1:
        if curIndex + 2 is len(c):
            numberOfJumps += 1
            break
        if c[curIndex + 1] is 0 and c[curIndex + 2] is 0:
            curIndex += 2
        elif c[curIndex + 1] is 1:
            curIndex += 2
        elif c[curIndex + 1] is 0 and c[curIndex + 2] is 1:
            curIndex += 1

        numberOfJumps += 1

    return numberOfJumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')
    fptr.close()
