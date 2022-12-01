# NOT WORKING YET

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list list
        final_list = []

        # base case
        if len(nums) == 1:
            return [nums[:]] # return all elements in the nums list

        # recursive case
        for i in range(len(nums)):
            num_case = nums.pop(0) # num_case = 0 
            

sol = Solution()
print(permute([1,2,3]))