class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}

        # Frequency of characters in s1
        for ch in s1:
            count[ch] = count.get(ch, 0) + 1

        window = {}
        left = 0
        right = 0

        while right < len(s2):
            # Add current character
            window[s2[right]] = window.get(s2[right], 0) + 1
            right += 1

            # Keep window size equal to len(s1)
            if right - left > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            # Check whether current window is a permutation
            if window == count:
                return True

        return False