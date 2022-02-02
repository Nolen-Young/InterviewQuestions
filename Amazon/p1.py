def getServedBuildings(buildingCount, routerLocation, routerRange):
    def isNegative(n: int) -> int: 
        if n <= 0: return 0
        else: return n
        
    def greaterThanMax(n: int, maxN: int) -> int:
        if n > maxN: return maxN
        else: return n
        
    # Write your code here
    service = [0] * len(buildingCount)
    maxIndex = len(buildingCount) - 1
    
    for i in range(len(routerLocation)):
        location = routerLocation[i] - 1
        rRange = routerRange[i]
        print(str(i) + " " + str(location))
        print(str(i) + " " + str(rRange))
        
        if rRange == 0:
            service[i] += 1
        else:
            for j in range(isNegative(location - rRange), greaterThanMax(location + rRange, maxIndex) + 1):
                service[j] += 1
    
    served = 0
    for i in range(len(service)):
        if service[i] >= buildingCount[i]:
            served += 1
            
    return served

buildingCount = [2, 1, 1, 3]
routerLocation = [1, 2]
routerRange = [2, 0]

# getServedBuildings(buildingCount, routerLocation, routerRange)

def wifiRouters(buildingCount, routerLocation, routerRange):
    service = [0] * len(buildingCount)
    length = len(buildingCount)
    rRange = bottom = top = 0

    for i in range(len(routerLocation)):
        rRange = routerRange[i]
        location = routerLocation[i]
        bottom = max(0, location - rRange - 1)
        top = min(length - 1, location + rRange - 1)

        service[bottom] += 1
        if top < length - 1:
            service[top + 1] -= 1

    print(service)
    for i in range(1, length):
        service[i] += service[i - 1]

    print(service)
    served = 0
    for i in range(1, len(buildingCount)):
        if service[i] >= buildingCount[i]:
            served += 1
    
    return served

print(wifiRouters(buildingCount, routerLocation, routerRange))


