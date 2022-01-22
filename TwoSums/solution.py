import sys

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Declare dictionary, which is a hash map. We can map the values to
        # their indexs to keep a list of the values we have seen.
        seenMap = {}
        
        for i, value in enumerate(nums):
            difference = target - value
            
            if difference in seenMap:
                return sorted([i, seenMap[difference]])
            
            seenMap[value] = i
            
        return 
            
if __name__ == '__main__':
    numList = sys.argv[1]
    target = sys.argv[2]
    if type(numList) == list and type(target) == int:
        if all(isinstance(x, int) for x in numList):
            print(Solution.twoSum(nums=numList, target=target))
            sys.exit()
        else:
            sys.exit(2)