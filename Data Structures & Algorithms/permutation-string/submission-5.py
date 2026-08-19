class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map={} 
        for i in s1:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        left = 0
        right=len(s1)

        window=s2[left:right]
        temp_window={}
        for i in window:
            if i in temp_window:
                temp_window[i]+=1
            else:
                temp_window[i]=1

        while right<len(s2):
            if map==temp_window:
                return True
            else:
                temp_window[s2[left]]-=1
                if temp_window[s2[left]]==0:
                    del temp_window[s2[left]]
                left+=1

                if s2[right] in temp_window:
                    temp_window[s2[right]]+=1
                else:
                    temp_window[s2[right]]=1
                right+=1
        return map==temp_window 