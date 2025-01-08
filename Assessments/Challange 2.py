#!/bin/python3

#import math
import os
#import random
#import re
#import sys



#
# Complete the 'findOverlappingTimes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def OLD_findOverlappingTimes(intervals):
    #Set up
    if not intervals:
        return []
    n = len(intervals)
    intervals.sort() #Organising data
    res = []
    
    #Checking for overlaps
    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1]
        
        #Skip already merged intervals
        if res and res[-1][1] >= end:
            continue
            
        #Find end of merged range
        for j in range(i +1, n):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
        res.append([start, end])
    
    return res

### Issues optential optimisation
# Efficiency merging: dont need to check repeatedly (maintain a current interval)
# Loops are very nested

def findOverlappingTimes(intervals):
    
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = []

    # Initialize the first interval
    current_start, current_end = intervals[0]

    for start, end in intervals[1:]:
        if start <= current_end:  # Overlapping intervals
            current_end = max(current_end, end)
        else:
            # No overlap; save the current interval and start a new one
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    # Append the last interval
    merged.append([current_start, current_end])
    return merged
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = findOverlappingTimes(intervals)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
