from math import log10

class Solution:
    def total_num_of_digits(self, num:int) -> int:

        # this also works only for positive numbers
        # not even for float or negative nums
        counter = 0
        while num > 0:
            counter += 1
            num = num // 10
        return counter

        # only valid for positive vals omly
        # if num == 0:
        #     return 1
        # count = int(log10(num) + 1)
        # return count

a = Solution()
print(a.total_num_of_digits(123))

# test-cases that failed:
# -123
# 123.45
