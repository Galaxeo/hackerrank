#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2] == 'P':
        if s[0:2] == '12':
            return s[0:-2]
        else:
            h = 12 + int(s[0:2])
    else:
        if s[0:2] == '12':
            h = '00'
        else:
            return s[0:-2]
    return str(h) + s[2:-2]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()
    s = "12:05:45AM"

    result = timeConversion(s)
    print(result)

    # fptr.write(result + '\n')
    #
    # fptr.close()

