#!/bin/python3

import math
import os
import random
import re
import sys

# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are

# Complete the sockMerchant function below.

def socksMatch(color1, color2):
    return color1 == color2

def sockMerchant(num_socks, socks):
    socksColorCount = {}
    pairsCount = 0
    
    for sock in socks:
        if sock in socksColorCount:
            socksColorCount[sock] += 1
        else:
            socksColorCount[sock] = 1
            
    for sockCount in socksColorCount.values():
        pairsCount += sockCount//2
        
    return pairsCount
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_socks = int(input())

    socks = list(map(int, input().rstrip().split()))

    result = sockMerchant(num_socks, socks)

    fptr.write(str(result) + '\n')

    fptr.close()