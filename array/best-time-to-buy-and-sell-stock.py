class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = prices[0]   # Minimum price seen so far
        max_profit = 0          # Maximum profit

        for i in range(1, len(prices)):

            # Update minimum buying price
            min_price = min(min_price, prices[i])

            # Calculate profit if sold today
            profit = prices[i] - min_price

            # Update maximum profit
            max_profit = max(max_profit, profit)

        return max_profit