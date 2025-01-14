def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = (num - min_val) // (max_val - min_val + 1) * bucket_count
        buckets[int(index)].append(num)
