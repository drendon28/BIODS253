from math import factorial

lines = 10
for row in range(lines):
    for column in range(lines-row+1):
        print(end=" ")

    for column in range(row+1):
        # nCr = n!/(n-r)!*r
        print(factorial(row)//(factorial(column)*factorial(row-column)), end=" ")

    print()