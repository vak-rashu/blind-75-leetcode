class Solution:
    def gcd(self, num1: int, num2: int):

        gcd_val = 0
        n = min(num1, num2)

        i = 1

        for i in range(n, i, -1):
            if num1 % i == 0 & num2 % i == 0:
                gcd_val = max(gcd_val, i)
                break

            i+=1

        return gcd_val

a = Solution()
print(a.gcd(3, 12))
# args = eval(input("Enter your value(q to quit): "))
# while args != "q":
#     print(a.gcd(num1, num2))
#     args = eval(input("Enter your value(q to quit): "))
