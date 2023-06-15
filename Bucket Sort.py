def bucketSort(arr):
    min_val = min(arr)
    max_val = max(arr)
    num_buckets = max_val - min_val + 1

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = num - min_val
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr


# Example usage
arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sorted_arr = bucketSort(arr)
print("Sorted array using Bucket Sort:", sorted_arr)
