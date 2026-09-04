# Encode and decode?
# How to hash multiple string in to one?
# Can you just append all in to one string and then hash them all using sha256?

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            number_part = str(len(string))
            denote_char = "$"
            text_part = string
            encoded = number_part + denote_char + text_part
            encoded_string+= encoded
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):

            if s[i].isdigit():
                
                cur_num = ""
                while s[i] != "$":
                    cur_num += s[i]
                    i+=1
                i+=1 # move pass the $ char
                cur_num = int(cur_num)
                cur_res = ""
                # Read the next cur_num nums of characters
                for j in range(cur_num):
                    cur_res += s[i]
                    i+=1
                res.append(cur_res)
        return res              
    