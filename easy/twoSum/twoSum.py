class Solution:
    def twoSum(self, nums, target: int):
        hashMap = {}
        diff = 0
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hashMap:
                return [hashMap[diff], i]
                break
            hashMap[nums[i]] = (i)