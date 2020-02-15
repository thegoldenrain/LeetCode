class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        
        for num in nums:
            check = 0
            
            while num > 0:
                num //= 10
                check += 1
                
            if check % 2 == 0:
                count += 1
                    
        return count


