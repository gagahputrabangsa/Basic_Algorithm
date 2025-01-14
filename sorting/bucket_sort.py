def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
