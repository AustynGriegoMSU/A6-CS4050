'''
Problem #1 Leetcode 518: Coin Change II
Problem Notes:
    Given amount and coins, find the number of combinations that make up that amount. 
    Assume that you have an infinite number of each kind of coin.

    Return 0 if not possible to make up the amount with the given coins.
    Return 1 if the amount is 0 or equal to one sole coin in the coins array.
    Else return # of combinations to make up the amount with the given coins.

    Dynamic Programming
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

    Dynamic Programming
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
    Each person has a different amount of money and a different level of quietness.
    richer[i] = [a, b] indicates that a is richer than b.
    All the given data in richer are logically correct; a richer than b, b will never be richer than a at same time.
    quiet[i] is the quietness of the i-th person.
    n = quiet.length = number of people
    
    Return an integer array answer where answer[x] = y if y is the least quiet person (that is, the person with the smallest quietness value) 
    among all people who definitely have equal to or more money than the x-th person.

    DFS, Graph
'''
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        answer = [-1] * n

        def dfs(node):
            if answer[node] != -1:
                return answer[node]

            minimum = node
            for neighbor in graph[node]:
                candidate = dfs(neighbor)
                if quiet[minimum] > quiet[candidate]:
                    minimum = candidate 
            answer[node] = minimum
            return minimum
        
        for a, b in richer:
            graph[b].append(a)

        return list(map(dfs, range(n)))
'''
Problem #4 Leetcode 1338: Reduce Array Size to The Half
Problem Notes:
    Given an array arr. 
    Choose a set of integers and remove all the occurrences of these integers in the array.

    Return the minimum size of the set so that at least half of the integers of the array are removed.

    Greedy (largest freq removed first), Hash Map
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        freq = sorted(count.values(), reverse=True)
        
        removed = 0
        ans = 0
        for f in freq:
            removed += f
            ans += 1
            if removed >= len(arr) // 2:
                return ans
            
        return ans