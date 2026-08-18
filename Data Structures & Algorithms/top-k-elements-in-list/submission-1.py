from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k most frequent number 
        numCounter = Counter(nums)

        # Sort the counter
        num = list(numCounter.items())
        
        num.sort(key=lambda x: x[-1], reverse=True)
        res = []
        for i in range(k):
            res.append(num[i][0])
        return res 