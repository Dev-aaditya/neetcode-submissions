class Solution:
    def trap(self, heights: List[int]) -> int:
        lm=rm=0
        water=0
        l=0
        r=len(heights)-1

        while l<r:

            if heights[l]<heights[r]:
                if lm<heights[l]:
                    lm=heights[l]
                else:
                    water+=lm-heights[l]
                l+=1

            else:
                if rm<heights[r]:
                    rm=heights[r]
                else:
                    water+=rm-heights[r]
                r-=1
        return water
