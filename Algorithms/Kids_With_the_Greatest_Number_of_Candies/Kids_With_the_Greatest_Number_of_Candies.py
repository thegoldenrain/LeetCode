class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        greatest = max(candies)
        
        for x in candies:
            if x + extraCandies >= greatest:
                output.append(True)
            else:
                output.append(False)

        return output
