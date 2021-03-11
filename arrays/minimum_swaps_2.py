#!/bin/python3

import os

# Complete the minimumSwaps function below.
def minimumSwaps(arr, n):
    
    swaps = 0
    
    # Save all elements to dictionary with indexes
    # to avoid searching for an index later
    # and reduce time complexity
    indexes = {value: index for index, value in enumerate(arr)}
    
    for i, value in enumerate(arr[:-1]):
        expected = i + 1
        value = arr[i]
        
        if value == expected:
            continue
        
        # Get the index of expected value and do the swap:
        j = indexes[expected]
        arr[i], arr[j] = arr[j], arr[i]
        
        # Update the indexes dictionary:
        indexes[expected] = i
        indexes[value] = j
        
        swaps += 1
    
    return swaps
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr, n)

    fptr.write(str(res) + '\n')

    fptr.close()
