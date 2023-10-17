class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if i == len(prices) - 1:
        #             return profit
        #         elif prices[j] > prices[i]:
        #             if (prices[j] - prices[i]) > profit:
        #                 profit = prices[j] - prices[i]

        min_price = prices[0]
        
        for price in prices[1:]:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)

        return profit

