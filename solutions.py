'''
Problem #1 Leetcode 518: Coin Change II
Problem Notes:
    Given amount and coins, find the number of combinations that make up that amount. 
    Assume that you have an infinite number of each kind of coin.

    Return 0 if not possible to make up the amount with the given coins.
    Return 1 if the amount is 0 or equal to one sole coin in the coins array.
    Else return # of combinations to make up the amount with the given coins.
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins:
            return 0
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]
        
'''
Problem #2 Leetcode 983: Minimum Cost For Tickets
Problem Notes:
    1-Day pass == costs[0]
    7-Day pass == costs[1]
    30-Day pass == costs[2]

    Return the minimum number of dollars you need to travel every day in the given list of days.
    Note days is strictly in increasing order (1 <= days[i] <= 365).
'''
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        ds = set(days)

        for i in range(1, len(dp)):
            if i not in ds:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2]
                )
        return dp[-1]
'''
Problem #3 Leetcode 851: Loud and Rich
Problem Notes:
    
'''

'''
Problem #4 Leetcode 1338: Reduce Array Size to The Half
Problem Notes:

'''