import random

# WIP NOT USABLE

class Solution:

    def generateParenthesis(self, n: int):
        # there n pairs of parenthesis
        # always start with an open parenthesis
        # if the open parenthesis > closed parenthesis, add a closed parenthesis
        # ex. n = 3, 3 open and 3 close parenthesis

        # have to use recursion for this
        
        randomNum = random.randint(0, 1)
            
        openP = "("
        openPCounter = 0
        closeP = ")"
        closePCounter = 0
        iParen = []
        allParen = []

sol = Solution()
print(sol.generateParenthesis(2))