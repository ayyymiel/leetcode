# NOT WORKING YET

class Solution:
    def arithmeticTriplets(self, nums: int, diff: int) -> int:
        checker1 = 0
        checker2 = 0
        validNums = []

        for i in range(len(nums)):
            i = (i+1)*-1
            checker1 = nums[i] - diff
            if checker1 in nums:
                checker2 = checker1 - diff
                if checker2 in nums:
                    validNums.append(nums[i])   # add the starting number
                    validNums.append(checker1)  # add the second number
                    validNums.append(checker2)  # add the last number to make the triplet

        tripletsCount = len(validNums) / 3
        return int(tripletsCount)

sol = Solution()
sol.arithmeticTriplets([0,1,4,6,7,10], 3)

# [0,1,4,6,7,10], diff = 3