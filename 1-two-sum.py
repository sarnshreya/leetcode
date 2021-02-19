class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            j = target-nums[i]
            if j in nums and nums.index(j) != i:
                result.append(i)
                result.append(nums.index(j))
                return result
                                        
