def isHappyNumber(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10
        n = total
    return n == 1

isHappyNum42 = isHappyNumber(42)
isHappyNum68 = isHappyNumber(68)
print(f"\n Happy Number 42 is : {isHappyNum42}. \n Happy Number 68 is : {isHappyNum68}.")