#!/bin/python3

import os

# Complete the rotLeft function below.
def rotLeft(a, d, n):
    new_a = []
    for index in range(n):
        new_a.append(a[d - n + index])

    return new_a
    # Neat solution from TChalla:
    # return a[d:] + a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
