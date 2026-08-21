# # actual approach: using Two pointers

# #   brute-force way
# # time-complexity: O(n^2)
# # space-complexity: O(1)
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_prof = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 prof = prices[j] - prices[i]
#                 max_prof = max(prof, max_prof)
        
#         return max_prof

# # two-pointers method
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         l, r = 0, 1
#         while r < len(prices):
#             if prices[l] < prices[r]:
#                 result = prices[r] - prices[l]
#                 max_profit = max(max_profit, result)
#             else:
#                 l = r
#             r += 1
#         return max_profit

# time-complexity: O(n)
# space-complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        buy, sell = 0, 1

        while sell < len(prices):
            print(sell, buy)
            prof = prices[sell] - prices[buy]
            print(prof, prices[sell], prices[buy])
            max_prof = max(max_prof, prof)
            # cond: not a profit
            if prices[sell] < prices[buy]:
                buy = sell
                sell+=1
                print(sell, buy)

            else:
                sell+=1

        return max_prof


a = Solution()
print(a.maxProfit([2, 1, 4]))