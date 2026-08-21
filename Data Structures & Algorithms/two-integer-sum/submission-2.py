class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index,value in enumerate(nums):
            needed = target-value
            if needed in map:
                return [map[needed],index]
            map[value]=index
            