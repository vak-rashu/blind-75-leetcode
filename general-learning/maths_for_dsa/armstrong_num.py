class Solution:
    def armstrong_num(self, num: int) -> bool:

        dup = num
        sum = 0

        while num > 0:

            digit = num % 10
            sum += digit**3
            num//=10

        if sum == dup:
            return True
        else:
            return False

a = Solution()
args = eval(input("Enter your value(q to quit): "))
while args != "q":
    print(a.armstrong_num(args))
    args = eval(input("Enter your value(q to quit): "))
