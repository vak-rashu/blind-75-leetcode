# my appraoch- brute force method

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                if curr_sum > max_sum:
                    max_sum = curr_sum

        return max_sum

# time-complexity: O(n^2)
# space-complexity: O(1)

# kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            curr_sum = max(curr_sum, 0)
            curr_sum += n
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
# time-complexity: O(n)
# space-complexity: O(1)