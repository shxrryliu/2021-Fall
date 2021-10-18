from ps1 import mergeSort, countSort, radixSort
from random import randrange
import time
# randint (a, b)

winners = {
    'merge' : [],
    'count' : [], 
    'radix' : []

}

counter = 0
for u_p in range (1, 20): 
    u = 2 ** u_p

    for n_p in range (1, 20):
        n = 2 ** n_p 

        test_arr = [(randrange(0, u, 1), i) for i in range(n)]

        start_time = time.time()
        mergeSort(test_arr)
        merge_time = time.time() - start_time

        start_time = time.time()
        countSort(test_arr, u)
        count_time = time.time() - start_time        

        start_time = time.time()
        radixSort(test_arr, n, u, n)
        radix_time = time.time() - start_time

        if min(merge_time, count_time, radix_time) == merge_time:
            winners['merge'].append((n_p, u_p))
        elif count_time < radix_time: 
            winners['count'].append((n_p, u_p))
        else: 
            winners['radix'].append((n_p, u_p))

        counter += 1
        print(counter)

print(winners)
print("final counter: " + str(counter))