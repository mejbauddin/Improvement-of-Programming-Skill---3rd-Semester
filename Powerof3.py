def isPowThree(n: int) -> bool:
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


print(isPowThree(1))
print(isPowThree(5))
print(isPowThree(27))