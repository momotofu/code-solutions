import math
import os
import random
import re
import sys

def countingValleys(n, s):
    # A valley or mountain is counted once sea level is
    # departed from and then returned to.
    # count steps from sea level

    altitude = 0
    valleys = 0

    for i in range(n):
        curStep = 1 if s[i] is 'U' else -1
        if altitude < 0 and altitude + curStep is 0:
            valleys += 1
        altitude += curStep

    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')
    fptr.close()

