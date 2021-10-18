from ps1 import mergeSort, countSort, radixSort
from random import randint
import time
# randint (a, b)

merge_times = {}
count_times = {}
radix_times = {}
iterations = 10 

for i in range(1, 21): 
    # length of universe
    u = 2 ** i 
    # length of the whole thing
    n = 2 ** i
    testnum = "test " + str(i)
    print(n)
    
    # construct sample array of key-item pair
    test_arr = []
    for i in range(n): 
        key = randint(1, u)
        item = i
        test_arr.append((key, item))

    # time function and update time in dict
    start_time = time.time()
    mergeSort(test_arr)
    merge_times[testnum] = (time.time() - start_time)

    start_time = time.time()
    countSort(test_arr, u)
    count_times[testnum] = (time.time() - start_time)
    
    start_time = time.time()
    radixSort(test_arr, n, u, n)
    radix_times[testnum] = (time.time() - start_time)

print("merge: " + str(merge_times))
print("count: " + str(count_times)) 
print("radix: " + str(radix_times))
