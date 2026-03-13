def bubbleSort(arr):
    arr = arr.copy()  # supaya list asli tidak berubah
    n = len(arr)

    total_comparisons = 0
    total_swaps = 0
    passes_used = 0

    for i in range(n):
        swapped = False
        passes_used += 1

        for j in range(0, n - i - 1):
            total_comparisons += 1

            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                total_swaps += 1
                swapped = True

        # cetak state array setelah setiap pass
        print(f"Pass {passes_used}: {arr}")

        # early termination
        if not swapped:
            break

    return (arr, total_comparisons, total_swaps, passes_used)


# Uji program
print("Input 1:")
result1 = bubbleSort([5, 1, 4, 2, 8])
print("Result:", result1)

print("\nInput 2:")
result2 = bubbleSort([1, 2, 3, 4, 5])
print("Result:", result2)
