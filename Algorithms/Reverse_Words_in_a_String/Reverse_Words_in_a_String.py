class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        out=""
        i = len(li)-1
        
        while i >= 0:
            out += li[i] + ' '
            i -= 1
            
        return out[:-1]
