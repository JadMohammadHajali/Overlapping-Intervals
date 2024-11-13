""" Overlapping Intervals Project

used to merge intervals
"""

def merge_intervals(interval):
    """
    :param interval: a list of integers of arrays
    :return: the merged intervals
    """
    overlapping = []

    for i in range(len(interval)-1):
        first_interval = interval[i]  # storing the first interval
        next_interval = interval[i+1]  # storing the next interval
        if first_interval[1] > next_interval[0]:  # compare the last element of array with first element of next array
            min_interval = min(first_interval)  # storing the lowest element of the first array
            max_interval = max(next_interval)  # storing the highest element of the next array
            overlapping.append([min_interval, max_interval])  # storing the new array
        else:
            overlapping.append(next_interval)
    return overlapping

Intervals = [[1,3], [2,4], [6,8],[7,9]]
print(merge_intervals(Intervals))
