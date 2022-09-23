class Solution:
    def __init__(self):
        self.hashMap = {}
        self.totalsList = []
        self.isInTotalsList = []
        self.tripletsCounter = 0
    def arithmeticTriplets(self, nums: int, diff: int) -> int:
        for i in range(len(nums)):
            self.hashMap[nums[i]] = i
            totalFromDiff = nums[i] + diff
            self.totalsList.append(totalFromDiff)

        for x in range(len(self.totalsList)):
           if self.totalsList[x] in self.hashMap.keys():
            print(self.totalsList)
            self.isInTotalsList.append(self.totalsList[x])

        print(self.isInTotalsList)
        return len(self.isInTotalsList) - 1
    
sol = Solution()
print(sol.arithmeticTriplets([4,5,6,7,8,9], 2))

# nums = [0,1,4,6,7,10], diff = 3