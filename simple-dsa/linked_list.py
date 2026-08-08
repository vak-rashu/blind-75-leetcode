class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = Node(None, head)

    def insert_node(self, value):
        node = Node(value=value, next=None)

        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next != None:
                print(curr.value)
                curr = curr.next

            curr.next = node
            print(curr.value)

    def traverse_list(self):
        curr = self.head
        while curr != None:
            print(curr.value, curr.next)
            if curr.next is None:
                break

            curr = curr.next

def main():

    l = LinkedList()
    l.insert_node(3)
    l.insert_node(45)
    l.insert_node(78)

    l.traverse_list()

main()
