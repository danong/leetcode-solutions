class Solution(object):
    def coinChange_bfs(self, coins, amount):
        """Breadth first search
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        visited = [False] * (amount + 1)
        num = 0
        cur_sum = [0]
        next_sum = []
        while cur_sum:
            num += 1
            for val in cur_sum:
                for coin in coins:
                    new_val = val + coin
                    if new_val == amount:
                        return num
                    if new_val < amount and not visited[new_val]:
                        next_sum.append(new_val)
                        visited[new_val] = True
            cur_sum, next_sum = next_sum, []
        return -1

    def coinChange_dp(self, coins, amount):
        """Dynamic programming
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coin_count = [0] + [float('inf')] * amount
        for coin in coins:
            for idx, val in enumerate(coin_count):
                if coin <= idx:
                    coin_count[idx] = min(val, 1 + coin_count[idx - coin])
        if coin_count[-1] == float('inf'):
            return -1
        else:
            return coin_count[-1]


a = Solution()
a.coinChange_dp([1, 2, 5], 11)
