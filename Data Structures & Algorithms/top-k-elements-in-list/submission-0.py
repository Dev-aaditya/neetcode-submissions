class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1

        sorted_keys = sorted(mp, key=mp.get, reverse=True)

        return sorted_keys[:k]