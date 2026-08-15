class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = set(nums)
        ans = 0
        for num in nums:
            if (num-1) not in map:
                count=1
                while num + count in map:
                    count += 1 
                if ans<count:
                    ans = count
                        
        return ans   