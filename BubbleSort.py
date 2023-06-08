# function for sorting array using bubble sorting algorithm
def BubbleSort(arr, start, end):
    end += 1
    for i in range(start, end):

        for j in range(0, end-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
