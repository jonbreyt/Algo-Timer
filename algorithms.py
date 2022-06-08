# Jacob Onbreyt
# EMPLID: 23756110
# Csc 22000 
# Programming Assignment 1     

import random
import time # module to keep track of time

arr1 = random.sample(range(1,11), 10)
arr2 = random.sample(range(1,101), 100)
arr3 = random.sample(range(1,1001), 1000)
arr4 = random.sample(range(1,10001), 10000)
arr5 = random.sample(range(1,100001), 100000)
arr6 = random.sample(range(1,1000001), 1000000)

# Insertion Sort
def insertionSort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    end_time = time.time()
    return end_time-start_time


print('For N = 10, time taken to execute insertion sort:', insertionSort(arr1))
print('For N = 100, time taken to execute insertion sort: ',insertionSort(arr2))
print('For N = 1000, time taken to execute insertion sort: ',insertionSort(arr3))
print('For N = 10000, time taken to execute insertion sort: ',insertionSort(arr4))
print('For N = 100000, time taken to execute insertion sort: ',insertionSort(arr5))
print('For N = 1000000, time taken to execute insertion sort: ',insertionSort(arr6))


# Merge Sort
def merge(arr, l, r, m):
    # make copies of both arrays 
    l_copy = arr[l:m + 1] # add one because second parameter is non inclusive
    r_copy = arr[m+1:r+1]

    l_copy_index = 0
    r_copy_index = 0
    sorted_index = l

    while l_copy_index < len(l_copy) and r_copy_index < len(r_copy):
        if l_copy[l_copy_index] <= r_copy[r_copy_index]:
            arr[sorted_index] = l_copy[l_copy_index]
            l_copy_index += 1
        else:
            arr[sorted_index] = r_copy[r_copy_index]
            r_copy_index += 1
        sorted_index += 1
    
    while l_copy_index < len(l_copy):
        arr[sorted_index] = l_copy[l_copy_index]
        l_copy_index += 1
        sorted_index += 1
    
    while r_copy_index < len(r_copy):
        arr[sorted_index] = r_copy[r_copy_index]
        r_copy_index += 1
        sorted_index += 1

def mergeSort(arr, l, r):
    start_time = time.time()
    if l >= r:
        return
    
    m = (l + r)//2
    mergeSort(arr, l, m)
    mergeSort(arr, m + 1, r)
    merge(arr, l, r, m)
    end_time = time.time()
    return end_time - start_time


print('For N = 10, time taken to execute merge sort:', mergeSort(arr1, 0, len(arr1)-1))
print('For N = 100, time taken to execute merge sort: ',mergeSort(arr2, 0, len(arr2)-1))
print('For N = 1000, time taken to execute merge sort: ',mergeSort(arr3, 0, len(arr3)-1))
print('For N = 10000, time taken to execute merge sort: ',mergeSort(arr4, 0, len(arr4)-1))
print('For N = 100000, time taken to execute merge sort: ',mergeSort(arr5, 0, len(arr5)-1))
print('For N = 1000000, time taken to execute merge sort: ',mergeSort(arr6, 0, len(arr6)-1))

# Heap Sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    start_time = time.time()
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    end_time = time.time()
    return end_time-start_time

print('For N = 10, time taken to execute heap sort:', heapSort(arr1))
print('For N = 100, time taken to execute heap sort: ',heapSort(arr2))
print('For N = 1000, time taken to execute heap sort: ',heapSort(arr3))
print('For N = 10000, time taken to execute heap sort: ',heapSort(arr4))
print('For N = 100000, time taken to execute heap sort: ',heapSort(arr5))
print('For N = 1000000, time taken to execute heap sort: ',heapSort(arr6))


# Quick Sort
def partition(arr, p, r):
    i = (p - 1)
    pivot = arr[p]
    for j in range(p, r):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j],arr[i]
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return (i + 1)

def quickSort(arr, p, r):
    start_time = time.time()
    if p < r:
        part = partition(arr, p, r)
        quickSort(arr, p, part-1)
        quickSort(arr, part+1, r)
    end_time = time.time()
    return end_time-start_time

print('For N = 10, time taken to execute quick sort:', quickSort(arr1, 0, len(arr1)-1))
print('For N = 100, time taken to execute quick sort: ',quickSort(arr2, 0, len(arr2)-1))
print('For N = 1000, time taken to execute quick sort: ',quickSort(arr3, 0, len(arr3)-1))
print('For N = 10000, time taken to execute quick sort: ',quickSort(arr4, 0, len(arr4)-1))
print('For N = 100000, time taken to execute quick sort: ',quickSort(arr5, 0, len(arr5)-1))
print('For N = 1000000, time taken to execute quick sort: ',quickSort(arr6, 0, len(arr6)-1))

# Quick Sort (random)    
def partitionRandomizer(arr, p, r):
    randpivot = random.randrange(p, r)
    arr[p], arr[randpivot] = arr[randpivot], arr[p]
    return partition(arr, p, r)

def partition(arr, p, r):
    pivot = p
    i = p + 1
    for j in range(p + 1, r +1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot], arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return (pivot)

def quickSortRandom(arr, p, r):
    start_time = time.time()
    if(p < r):
        pivotindex = partitionRandomizer(arr, p, r)
        quickSortRandom(arr, p, pivotindex - 1)
        quickSortRandom(arr, pivotindex + 1, r)
    end_time = time.time()
    return end_time-start_time

print('For N = 10, time taken to execute quick sort random:', quickSortRandom(arr1, 0, len(arr1)-1))
print('For N = 100, time taken to execute quick sort random: ',quickSortRandom(arr2, 0, len(arr2)-1))
print('For N = 1000, time taken to execute quick sort random: ',quickSortRandom(arr3, 0, len(arr3)-1))
print('For N = 10000, time taken to execute quick sort random: ',quickSortRandom(arr4, 0, len(arr4)-1))
print('For N = 100000, time taken to execute quick sort random: ',quickSortRandom(arr5, 0, len(arr5)-1))
print('For N = 1000000, time taken to execute quick sort random: ',quickSortRandom(arr6, 0, len(arr6)-1))


# Radix Sort
def countingSort(arr, place):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)

    for i in range(0, n):
        index = (arr[i]/place)
        count[int((index)%10)] += 1
    
    for i in range(1, 10):
        count[i] += count[i-1]
    
    i = n-1
    while i >= 0:
        index = (arr[i]/place)
        output[count[int((index)%10)] - 1] = arr[i]
        count[int((index)%10)] -= 1
        i -= 1
    
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    start_time = time.time()
    max1 = max(arr)
    exp = 1
    while max1/exp > 0:
        countingSort(arr, exp)
        exp *= 10
    end_time = time.time()
    #return end_time-start_time
    return arr

print(radixSort(arr1))
    






