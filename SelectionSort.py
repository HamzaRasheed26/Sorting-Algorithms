# function for sorting array using selection sorting algorithm
def SelectionSort(array, start, end):
    for i in range(start,end+1):        # this loop is for selecting a number index and compare the number than other
        idx = i                      # storing index into variable idx 
        for x in range(i, end+1): # this loop for selecting all numbers to compare with idx number
            if array[idx] > array[x]:    # checking number on idx is greater than number on x
                idx = x              # if greater than chsnge idx to i
        temp = array[i]                
        array[i] = array[idx]
        array[idx] = temp
    return array