from difflib import Differ


def DifferenceSumSquary(n: int) -> int:
    sumSquare = squareSum = 0
    for i in range(n):
        temp = i + 1
        sumSquare += temp**2
        squareSum += temp
    squareSum = squareSum**2
    return(squareSum - sumSquare)

print(DifferenceSumSquary(100))