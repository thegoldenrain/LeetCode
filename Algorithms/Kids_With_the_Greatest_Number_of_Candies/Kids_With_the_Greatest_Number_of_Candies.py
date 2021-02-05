class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        
        for x in candies:
            if x + extraCandies >= max(candies):
                output.append(True)
            else:
                output.append(False)

        return output
