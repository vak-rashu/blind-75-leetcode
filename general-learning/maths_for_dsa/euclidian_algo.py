class Solution:
    def euclidian_algo(self, num1, num2):

        # not an efficient way
        # because we are creating the diff and very small diffs again and again
        # if num2 == 0:
        #     return num1

        # if num1 < num2:
        #     temp = num1
        #     num1 = num2
        #     num2 = temp

        # return self.euclidian_algo(num1-num2, num2)


        # this is an efficient way because
        # we are directly reaching to a point where
        # the diff is the remainder of the two nums
        if num2 == 0:
            return num1

        return self.euclidian_algo(num2, num1 % num2)

a = Solution()

print("Pls enter you values")
arg1 = eval(input("Enter your value 1(q to quit): "))
arg2 = eval(input("Enter your value 2(q to quit): "))
while arg1 != "q":
    print(a.euclidian_algo(arg1, arg2))
    # args = eval(input("Enter your value(q to quit): "))
    print("Pls enter you values")
    arg1 = eval(input("Enter your value 1(q to quit): "))
    arg2 = eval(input("Enter your value 2(q to quit): "))
