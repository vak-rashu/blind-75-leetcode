class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = nums[0]
        curr_prod = nums[0]

        for n in nums[1:]:
            
            if min_prod > curr_prod * n:
                min_prod = min(min_prod, curr_prod*n)
            else:
                min_prod = 1

            curr_prod = n * min_prod

        return curr_prod

nums = [2, 3, -2, 4]
sum = Solution()
print(sum.maxProduct(nums))
