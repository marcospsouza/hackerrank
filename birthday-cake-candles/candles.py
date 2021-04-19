#!/bin/python3

import math
import os
import random
import re
import sys

#You are in charge of the cake for a child's birthday. 
# You have decided the cake will have one candle for each year of their total age. 
# They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

#Example: candles = [4, 4, 1, 3]

#The maximum height candles are  units high. There are  of them, so return .

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    candlesDict = dict.fromkeys(candles, 0)
    
    for candle in candles:
        candlesDict[candle] += 1
        
    return candlesDict[max(candlesDict)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()