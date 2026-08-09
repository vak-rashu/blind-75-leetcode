class Solution:
    def func_name(self, num: int) -> bool:

        copy_num = num
        rev_num = 0
        while num > 0:
            last_digit = num % 10
            rev_num = (rev_num*10) + last_digit
            num//=10
        
        if rev_num == copy_num:
            return True
        else:
            return False

a = Solution()
args = eval(input("Enter your value(q to quit): "))

while args != "q":
    print(a.func_name(args))
    args = eval(input("Enter your value(q to quit): "))
