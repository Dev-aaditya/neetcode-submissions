class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        i=0
        r=len(heights)-1
        while i<r:
            length=r-i
            width=min(heights[i],heights[r])
            temp=length*width
            if temp>max:
                max=temp
            if heights[r]<heights[i]:
                r-=1
            else:
                i+=1   
                
        return max