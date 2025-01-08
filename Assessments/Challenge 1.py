#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findFirstUnique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.

### Low case only
# return the index using 1-base indexing
# If no unique characters return -1

def findFirstUnique(s):
    # Create a dictionary to count character occurrences
    char_count = {}

    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate through the string and find the first unique character
    for idx, char in enumerate(s):
        if char_count[char] == 1:
            # Return the index as 1-based
            return idx + 1

    # If no unique character is found, return -1
    return -1
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = findFirstUnique(s)

    fptr.write(str(result) + '\n')

    fptr.close()
