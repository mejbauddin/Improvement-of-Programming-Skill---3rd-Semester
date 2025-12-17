

def increasingTriplet(nums: list[int]) -> bool:
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

nums1 = [2, 1, 5, 0, 4, 6]
print(increasingTriplet(nums1))
nums2 = [5, 4, 3, 2, 1]
print(increasingTriplet(nums2))



print(float('inf'))