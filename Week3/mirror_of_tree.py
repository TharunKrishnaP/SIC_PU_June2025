class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
    return root

def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data, end=" ")
    in_order_traversal(node.right)

def invert_tree(root):
    if root is None:
        return None
    # Swap left and right recursively
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

# Input tree nodes
input_nodes = list(map(int, input("Enter node values: ").split()))

# Build the tree
root = None
for val in input_nodes:
    root = insert_node(root, val)

print("In-order traversal before inversion:")
in_order_traversal(root)

# Invert the tree
invert_tree(root)

print("\nIn-order traversal after inversion:")
in_order_traversal(root)