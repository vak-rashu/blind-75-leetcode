class Solution:
    def armstrong_num(self, num: int) -> bool:

        count, sum = 0, 0
        dup = num

        while num > 0:
            count +=1
            num//=10

        num = dup

        while num > 0:
            digit = num % 10
            digit = digit ** count
            sum += digit
            num //= 10

        if sum == dup:
            return True
        else:
            return False

a = Solution()
args = eval(input("Enter your value(q to quit): "))
while args != "q":
    print(a.armstrong_num(args))
    args = eval(input("Enter your value(q to quit): "))
