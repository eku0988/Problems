# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    key = arr[-1]  # last element
    i = n - 2

    # Shift elements one by one until correct position is found
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]   # shift right
        print(*arr)           # print current state
        i -= 1

    arr[i + 1] = key  # place key at correct position
    print(*arr)       # final array print

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)
