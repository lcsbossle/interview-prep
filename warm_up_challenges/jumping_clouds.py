#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, steps=0):
    
    if len(c) == 1:
        return steps
    
    elif len(c) == 2:
        return steps + 1
    
    elif c[2] == 0:
        return jumpingOnClouds(c[2:], steps + 1)
    
    else:
        return jumpingOnClouds(c[1:], steps + 1)
    
if __name__ == '__main__':
    clouds = sys.argv[1:]
    c = list(map( lambda x: int(x), clouds) )

    result = jumpingOnClouds(c)
    print(result)

