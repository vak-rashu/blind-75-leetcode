class Solution:
    def reverse_number(self, num: int) -> int:

        rev_num = 0

        while num > 0:
            last_digit = num % 10
            rev_num = (rev_num*10) + last_digit
            num//=10

        return rev_num

a = Solution()
print(a.reverse_number(900))
