#arr is array of (val, key) pairs
import math
import time
import random


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)


def countSort(arr, univsize):
    universe = []
    for i in range(univsize + 1):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr


def useCountSort(arr, b, i): 
    temp_array = []
    for elt in arr:
        place_val = (elt[0] // (b ** i)) % b
        temp_array.append((place_val, elt[1], elt[0]))
    temp_arr = countSort(temp_array, b)

    output_arr = []
    for elt in temp_arr: 
        output_arr.append((elt[2], elt[1]))
    return output_arr

def radixSort(arr, n, U, b): 
    # to be clear, n = length of the array, and also the base
    # find amount of digits
    # needs to do floor + 1 because for certain examples like 
        # 100 with base 10 we would get digits = 2, but it's actually 3
    digits = math.floor(math.log(U, b)) + 1

    # create a copy of the array to sort
    output_arr = arr 
    # use Count Sort by digit!
    for i in range(0, digits): 
        output_arr = useCountSort(output_arr, b, i)
    return output_arr

# arr = [(170, 'a'), (45, 'b'), (75, 'c'), (90, 'd'), (24, 'f'), (2, 'g'), (66, 'h')]

# print(radixSort(arr, 10, 200, 10))