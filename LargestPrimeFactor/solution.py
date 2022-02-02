def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    
    for i in range(2, n // 2 + 1):
        if n % i == 0: return False

    return True

num = 600851475143
result = 0

for i in range(num // 2 + 1, 1, -1):
    if num % i == 0:
        if isPrime(i):
            result = i
            break

print(result)