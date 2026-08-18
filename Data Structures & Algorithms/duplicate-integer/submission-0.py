from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = defaultdict(int)
        
        for num in nums:
            if numDict[num] >= 1:
                return True
            else:
                numDict[num] +=1
        return False