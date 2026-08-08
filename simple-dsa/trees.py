
class TreeNode:
    def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def insert_node(self, value):
        if self.data < value:
            if self.right == None:
                self.right = TreeNode(value)
            else:
                self.right.insert_node(value=value)

        elif self.data > value:
             if self.left == None:
                self.left = TreeNode(value)
             else:
                self.left.insert_node(value=value)

    def traverse(self):
        #inorder traverse
        # if self.left is not None:
        #     self.left.traverse()

        # print(self.data)

        # if self.right is not None:
        #     self.right.traverse()

        # preorder traversel

        # if self.data:
        #     print(self.data)

        # if self.left != None:
        #     self.left.traverse()

        # if self.right != None:
        #     self.right.traverse()

        pass

def main():

    tree = TreeNode(10)

    tree.insert_node(4)
    tree.insert_node(5)
    tree.insert_node(11)
    tree.insert_node(12)
    tree.insert_node(-1)

    tree.traverse()

main()
