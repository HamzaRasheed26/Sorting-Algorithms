def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(n):
        arr[i] = output[i]

def radixSort(arr):
    max_value = max(arr)
    exp = 1

    while max_value // exp > 0:
        countingSort(arr, exp)
        exp *= 10


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
radixSort(arr)
print("Sorted array using Radix Sort:", arr)