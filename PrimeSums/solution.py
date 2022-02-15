def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    
    for i in range(2, n // 2 + 1):
        if n % i == 0: return False

    return True

def primeSums(n: int) -> int:
    result = 0

    for i in range(n): 
        if isPrime(i): result += i
    
    return result


print(primeSums(2000000))