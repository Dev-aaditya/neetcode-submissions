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
        while right<=len(s2):
            window=s2[left:right]
            temp_window={}
            for i in window:
                if i in temp_window:
                    temp_window[i]+=1
                else:
                    temp_window[i]=1
            if map==temp_window:
                return True
                
            left, right = left+1 , right+1
        return False 