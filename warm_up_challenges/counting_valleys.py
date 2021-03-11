#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    # Write your code here
    level = 0
    valleys = 0
    
    for step in path:
        if level == 0 and step == 'D':
            valleys += 1
        
        if step == 'U': level -= 1
        elif step == 'D': level += 1
    
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

