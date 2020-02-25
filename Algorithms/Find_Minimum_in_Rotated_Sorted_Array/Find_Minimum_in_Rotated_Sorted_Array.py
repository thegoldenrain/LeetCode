class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        
        for i in range(1, len(nums)):
            if minNum > nums[i]:
                minNum = nums[i]
        
        return minNum
