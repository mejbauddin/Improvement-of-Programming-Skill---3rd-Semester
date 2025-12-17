def titleToNum(colTitle: str) -> int:
    result = 0
    for char in colTitle:
        result = result * 26 + (ord(char) - ord('A') + 1)
    return result

print(titleToNum("X"),titleToNum("AZ"),titleToNum("BC"))