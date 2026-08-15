class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l=sorted(nums)
        k = 0-k
        return l[k]