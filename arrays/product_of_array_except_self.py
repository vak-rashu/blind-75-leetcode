# my approach: slice the list but used math modul

import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        for i in range(len(nums)):
            new_list = nums[0:i] + nums[i+1:]
            result = math.prod(new_list)
            product.append(result)
        return product

# time complexity: O(n)
# space complexity: O(n)


# actual solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * (len(nums))
        postfix = [0] * (len(nums))

        final = []

        prefix[0] = 1
        postfix[len(postfix) - 1] = 1

        prod1 = prod2 = 1
        for i in range(1, len(nums)):
            prod1 *= nums[i-1]
            prefix[i] = prod1
        
        for i in range(len(nums)-2, -1, -1):
            prod2 *= nums[i+1]
            postfix[i] = prod2
        
        for i in range(0, len(nums)):
            final.append(prefix[i]*postfix[i])
        return final

# time complexity: O(n)
# space complexity: O(n)
