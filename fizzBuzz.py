def fizzBuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

fizzBuzz3 = fizzBuzz(3)
fizzBuzz5 = fizzBuzz(5)
fizzBuzz15 = fizzBuzz(15)
     
print(fizzBuzz3)
print(fizzBuzz5)
print(fizzBuzz15)