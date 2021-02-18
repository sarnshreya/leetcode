class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        for each in range(0, len(nums)):
            i ^= nums[each]
        return i
