def ss(arr):
    for i in range(len(arr)):
        mnin=arr.index(min(arr[i:]))
        mn = min(arr[i:])
        arr[i], arr[mnin] = arr[mnin], arr[i]
    return arr