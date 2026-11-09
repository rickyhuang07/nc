class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse = True)
        initial = piles[0]
        res = initial
        left, right = 1, initial
        while left <= right:
            count = 0
            mid = (left + right) // 2
            for pile in piles:
                count += math.ceil(pile / mid)
            if count <= h:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res
        