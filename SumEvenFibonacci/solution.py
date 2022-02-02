result = summed = 0
fib1 = fib2 = 1

while result < 4000000:
    if result % 2 == 0:
        summed += result

    result = fib1 + fib2
    fib1 = fib2
    fib2 = result

print(summed)


