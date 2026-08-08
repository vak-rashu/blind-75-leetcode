class Stack:
    def __init__(self):
        self.stack = []

    def push_stack(self, ele):
        self.stack.append(ele)

    def pop_stack(self):

        if len(self.stack) == 0:
            return "Underflow Error: Cant evaluate items"

        lastIndex = len(self.stack) - 1
        # popped_element = self.stack[lastIndex]
        # self.stack = self.stack[:lastIndex]

        popped_element = self.stack.pop(lastIndex)

        return (f"Popped element: {popped_element}\nNew Stack is: {self.stack}")

def main():

    a = Stack()
    a.push_stack(5)
    a.push_stack(4)
    a.push_stack(6)
    a.push_stack(7)
    a.push_stack(8)

    print(a.stack)

    print(a.pop_stack())
    print(a.pop_stack())

    print(a.stack)

main()
