from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount == 1:
            if 1 in coins:
                return 1
            else: return -1
        coins = list(set(coins))
        coins.sort()
        num_coins = 0

        def rec_fine(amount):
            if len(coins) == 0:
                return -1
            nonlocal num_coins
            if coins[-1] == amount:
                num_coins += 1
                return 1
            if coins[-1] > amount:
                coins.pop()
                return rec_fine(amount)
            if rec_fine(amount - coins[-1]):
                num_coins += 1
            else:
                if len(coins):
                    coins.pop()

        rec_fine(amount)
        return num_coins




def main():
    s = Solution()
    result = s.coinChange([1,2,5], 16)
    print(result)

if __name__ == '__main__':
    main()