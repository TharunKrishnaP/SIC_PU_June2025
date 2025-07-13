class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class BST:
    def __init__(self):
        self.root = None

    def insert_node(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = Node(data) # type: ignore
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(data) # type: ignore
                    break
                current = current.right
    
    def height_of_tree(self,root):
        while root is None:
            return -1
        left_height = self.height_of_tree(root.left)
        right_height = self.height_of_tree(root.right)
        height = max(left_height, right_height) + 1
        return height
bst = BST()
node_list = list( map(int, input("Enter values: ").split()))
for i in node_list:
    bst.insert_node(i)
height = bst.height_of_tree(bst.root)
print("Height of given tree : ", height)