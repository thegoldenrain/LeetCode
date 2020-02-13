class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for num in nums:
            check = 0
            
            while num > 0:
                num = num // 10
                check = check + 1
                
            if check % 2 == 0:
                count = count + 1
                    
        return count
