class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map={0:1}
        freq=0
        curr_sum=0
        for num in nums:
            curr_sum+=num
            if curr_sum-k in map:
                freq+=map[curr_sum-k]
            map[curr_sum]=map.get(curr_sum,0)+1
        return freq