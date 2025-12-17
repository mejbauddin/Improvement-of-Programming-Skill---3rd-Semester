



def rotateArray(nums: list[int], k: int) -> None:
    n = len(nums)
    k = k % n  
    nums[:] = nums[-k:] + nums[:-k]


nums = [0, 1, 2, 3, 4]
rotateArray(nums, 8)
print("current array:", nums)