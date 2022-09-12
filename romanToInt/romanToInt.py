class Solution:
    def __init__(self):
        self.letter_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        self.running = 0
    def romanToInt(self, s: str) -> int:
        splitString = [*s]
        splitValues = []
        
        for i in range(len(splitString)):
            if splitString[i] in self.letter_dict.keys():
                splitValues.append(self.letter_dict[splitString[i]])
                
        for i in range(len(splitValues)-1):
            try:
                if splitValues[i] < splitValues[i+1]:
                    new_val = splitValues[i+1] - splitValues[i]
                    splitValues.pop(i+1)
                    splitValues.pop(i)
                    splitValues.insert(i, new_val)
                    print(splitValues)
                    print(splitValues)
            except IndexError:
                pass
    
        for i in range(len(splitValues)):   
            self.running += splitValues[i]
        
        return self.running

sol = Solution()
sol.romanToInt('MCMXCIV')
