class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        n=len(s1)
        right=left+n
        while right<=len(s2):
            temp=''
            for i in range(left,right):
                temp+=s2[i]
            if "".join(sorted(s1))=="".join(sorted(temp)):
                return True
            left, right = left+1 , right+1
        return False 