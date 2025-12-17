def trailingZeros(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


trailingZeros3 = trailingZeros(3)
trailingZeros5 = trailingZeros(5)
trailingZeros10 = trailingZeros(10)

print(trailingZeros3)
print(trailingZeros5)
print(trailingZeros10)