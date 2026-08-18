class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = temp = 0
        s=0
        f=s+1
        while f<len(prices):
            if prices[f]<prices[s]:
                s=f
            temp=prices[f]-prices[s]
            if temp>ans:
                ans=temp
            f+=1
        return ans
            