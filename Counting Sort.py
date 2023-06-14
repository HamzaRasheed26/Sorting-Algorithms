import random


def reverse_array(array):
    arr = [0]*len(array)

    k = 0
    for i in range(len(array)-1, -1, -1):
        arr[k] = array[i]
        k += 1
    return arr


def CountingSort(arr, order):
    size = max(arr)

    output = [0] * len(arr)

    # Initialize count array
    count = [0] * (size+1)

    # Store the count of each elements in count array
    for i in range(0, len(arr)):
        count[arr[i]] += 1

    # Store the cummulative count
    for i in range(1, size+1):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, len(arr)):
        arr[i] = output[i]
    if order == "Des":
        return reverse_array(arr)
    return arr


def RandomArray(size):
    arr = []
    for i in range(size):
        num = random.randint(0, 100)
        arr.append(num)
    return arr


arr = RandomArray(20)
print(arr)

CountingSort(arr, "Asc")
print(arr)
