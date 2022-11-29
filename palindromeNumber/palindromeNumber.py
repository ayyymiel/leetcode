class Solution:
    def isPalindrome(self, x: int) -> bool:
        forwards = []
        backwards = []
        itIs : bool
        toStrX = str(x)
        for i in range(len(toStrX)):
            forwards.append(toStrX[i])
        
        for g in range(len(toStrX)):
            g += 1
            g = g*-1
            backwards.append(toStrX[g])

        if forwards == backwards:
            itIs = True
        else:
            itIs = False

        return itIs

sol = Solution()
print(sol.isPalindrome(10001))