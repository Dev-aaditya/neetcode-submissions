class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[r]+nums[l]
                target=nums[i]*(-1)
                if sum==target:
                    ans.append([nums[l],nums[r],nums[i]])
                    r-=1
                    l+=1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum<target:
                    l+=1
                else:
                    r-=1
                    
        return ans