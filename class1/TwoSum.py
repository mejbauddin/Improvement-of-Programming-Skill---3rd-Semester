

def posOfTwoAddends(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return [-1, -1]


nums = [2,7,11,15]
print(posOfTwoAddends(nums, 9))
print(posOfTwoAddends(nums, 18))
print(posOfTwoAddends(nums, 10))

