x0 = [1, 2, 3, 3, 4, 5, 5, 7, 7]

# Part a
x1 = [num ** 2 for num in x0]

# Part b
x2 = [num for num in x1 if num % 2 != 0]

# Part c
x3 = sorted(list(set(x2)))

# Part d
res = 1
for num in x3:
    res *= num



print(x1)
print(x2)
print(x3)
print(res)