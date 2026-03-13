# Metode Naive (Brute Force) — O(n²)

def countInversionsNaive(arr):
    count = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


# Metode Smart (Merge Sort) — O(n log n)

def merge_and_count(left, right):
    i = j = 0
    merged = []
    inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inv_count


def merge_sort_count(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort_count(arr[:mid])
    right, inv_right = merge_sort_count(arr[mid:])

    merged, inv_merge = merge_and_count(left, right)

    return merged, inv_left + inv_right + inv_merge


def countInversionsSmart(arr):
    _, count = merge_sort_count(arr)
    return count

# Menguji Kedua Fungsi

import random
import time

sizes = [1000, 5000, 10000]

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]

    start = time.time()
    naive = countInversionsNaive(arr)
    t1 = time.time() - start

    start = time.time()
    smart = countInversionsSmart(arr)
    t2 = time.time() - start

    print("Size:", size)
    print("Naive:", naive, "Time:", t1)
    print("Smart:", smart, "Time:", t2)
    print()
