class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        prev = 0
        
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        for i in range(len(s)):
            if dic[s[i]] > prev:
                num += dic[s[i]] - prev - prev
            else:
                num += dic[s[i]]
                
            prev = dic[s[i]]
            
        return num
    
