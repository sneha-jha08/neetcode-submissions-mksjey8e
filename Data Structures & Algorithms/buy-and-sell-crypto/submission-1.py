class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof=0
        prof=0
        # prof= cp-sp
        for i  in range(len(prices)):
            for j in range(len(prices)):
                if i<j:
                    prof=prices[j]-prices[i]
                    if prof>max_prof:
                        max_prof=prof
        return max_prof

        