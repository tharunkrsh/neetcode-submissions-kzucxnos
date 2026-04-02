class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit=0
        while r<len(prices):
            print(f'round {r}')
            if prices[r]-prices[l]>=0:
                if prices[r]-prices[l]>profit:
                    profit=prices[r]-prices[l]
                    print(profit)
                r+=1
            else:
                print(l, r)
                l = r
                r += 1
            
        return profit


        
