class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof=0
        cp, sp=0,1
        while sp<len(prices):
            if prices[sp]>prices[cp]:
                prof=prices[sp]-prices[cp]
                max_prof=max(prof,max_prof)
            else:
                cp=sp
            sp+=1
        return max_prof

        