

def findkthlargest(arr: list[int], k: int) -> int:
    arr.sort(reverse=True)
    return arr[k-1]

print(findkthlargest([3, 2, 1, 5, 6, 4], 2))  
print(findkthlargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  