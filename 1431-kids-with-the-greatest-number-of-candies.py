class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = []
        for has in candies:
            if has+extraCandies >= mx:
                res.append(True)
            else:
                res.append(False)
        return res
        