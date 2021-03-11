#!/bin/python3


# Complete the minimumBribes function below.
def minimumBribes(q, n):
    b = 0
    
    for i in range(n):
        #Check if a person bribed more than 2 times:
        if q[i] > i + 3:
            print("Too chaotic")
            return
        # For each person in front of the current i, check if i was bribed
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]: b += 1
    print(b)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q, n)

