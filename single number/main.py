class Solution:
    def singleNumber(self, nums) -> int:
        return 2 * sum(set(nums)) - sum(nums)

numss = [2,2,1]
