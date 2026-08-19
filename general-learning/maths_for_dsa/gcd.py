class Solution:
    def gcd(self, num1: int, num2: int):

        gcd_val = 0
        n = min(num1, num2)

        for i in range(n, 0, -1):
            if (num1 % i == 0 and num2 % i == 0):
                gcd_val = max(gcd_val, i)
                break

        # return gcd_val
        print(gcd_val)

a = Solution()
a.gcd(199, 98)
# args = eval(input("Enter your value(q to quit): "))
# while args != "q":
#     print(a.gcd(num1, num2))
#     args = eval(input("Enter your value(q to quit): "))
