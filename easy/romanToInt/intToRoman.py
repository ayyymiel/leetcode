class Solution:
    def __init__(self):
        self.letter_dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

    def intToRoman(self, num: int) -> str:
        num = str(num)
        splitNum = [*num]
        splitLett = []

        splitNum = (list(map(int, splitNum)))

        for nums in range(len(splitNum)):
            int(splitNum[nums])
            if splitNum[nums] in self.letter_dict.keys():
                splitLett.append(self.letter_dict[splitNum[nums]])

        return splitLett

sol = Solution()
print(sol.intToRoman(51))