
def sort012(arr: list[int]) -> None:
    count = [0, 0, 0]
    for num in arr:
        count[num] += 1
    index = 0
    for i in range(3):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1

a = [2, 0, 1, 0, 1, 1, 2]
sort012(a)
print(a)  