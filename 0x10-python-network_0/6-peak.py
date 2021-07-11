#!/usr/bin/python3
"""Peak element"""


def find_peak(list_of_integers):
    """find a peak element in a list of integers"""
    if not list_of_integers:
        return None
    arr = list_of_integers
    peak = arr[0]
    for i in range(0, len(arr) - 1):
        if arr[i+1] > arr[i]:
            peak = arr[i + 1]
        if arr[i - 1] < arr[i - 2]:
            peak = arr[i - 2]
        return peak

