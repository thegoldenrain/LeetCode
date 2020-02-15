class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        newList = []
        
        while i < len(nums):
            for j in range(nums[i]):
                newList.append(nums[i + 1]) 
                
            i = i + 2
            
        return newList
