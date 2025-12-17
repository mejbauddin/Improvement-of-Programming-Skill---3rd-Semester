
def findConvex(arr: list[int]) -> int:
    n = len(arr)
    for i in range(n):
        left = arr[i-1] if i > 0 else float('-inf')
        right = arr[i+1] if i < n-1 else float('-inf')
        if left <= arr[i] and right <= arr[i] and (left < arr[i] or right < arr[i]):
            return i
    return -1

a = [1, 1, 1]
print(findConvex(a))  


b = [1, 2, 3, 2, 1]
print(findConvex(b))  

c = [1, 2, 3, 4]
print(findConvex(c))  