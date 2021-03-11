#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    for line in range(4):
        for col in range(4):
            sums.append(
                        arr[line][col] + arr[line][col+1] + arr[line][col+2] +
                        arr[line+1][col+1] +
                        arr[line+2][col] + arr[line+2][col+1] + arr[line+2][col+2]
                    )
    return max(sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

