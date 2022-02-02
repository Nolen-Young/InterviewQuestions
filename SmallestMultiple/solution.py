def SmallestMultiple(n: int):
    i = n
    while True:
        for j in range(n):
            if i % (j + 1) != 0: break
            elif j + 1 == n: return i

        i += 1

print(SmallestMultiple(20))