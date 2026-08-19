class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        left=0
        max_freq=0
        ans=0
        for right in range(len(s)):

            if s[right] in map:
                map[s[right]]+=1
            else:
                map[s[right]]=1

            max_freq=max(max_freq, map[s[right]])

            while (right-left)+1 - max_freq>k:
                map[s[left]]-=1
                left+=1

            ans = max(ans,(right-left)+1)

        return ans
        