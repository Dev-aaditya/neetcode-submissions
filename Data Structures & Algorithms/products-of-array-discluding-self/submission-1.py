class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre*=nums[i]
        nex = 1
        for i in range(len(nums))[::-1]:
            res[i] *= nex
            nex*=nums[i]
        return res