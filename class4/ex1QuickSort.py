def quickSort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]  
    left = [x for x in arr[:-1] if x <= pivot]  
    right = [x for x in arr[:-1] if x > pivot]  
    return quickSort(left) + [pivot] + quickSort(right)

print(quickSort([9, 7, 8, 4, 1, 2, 3, 8, 0, 5]))