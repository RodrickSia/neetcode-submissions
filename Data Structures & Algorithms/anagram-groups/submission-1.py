from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hash function that take into account the ascii values of these character? 
        
        # you can sort the char but is it optimal ? length of the string is very sort so it is good
        
        wordGroups = defaultdict(list)
        for word in strs:        
            group_index = hash("".join(sorted(word)))
            # create dict with the key being the group index
            wordGroups[group_index].append(word)
        return list(wordGroups.values())