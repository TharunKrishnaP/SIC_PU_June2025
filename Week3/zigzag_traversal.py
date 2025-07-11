class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree(node_relations):
    nodes = {}
    root = None
    for parent, child, side in node_relations:
        if parent not in nodes:
            nodes[parent] = Node(parent)
        if child not in nodes:
            nodes[child] = Node(child)
        
        if side == "L":
            nodes[parent].left = nodes[child]
        elif side == "R":
            nodes[parent].right = nodes[child]
        
        # First node as root
        if root is None:
            root = nodes[parent]
    return root

def zigzag_traversal(root):
    if not root:
        return []
    result = []
    current_level = [root]
    left_to_right = True
    while current_level:
        level_values = []
        next_level = []
        for node in current_level:
            level_values.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if not left_to_right:
            level_values.reverse()
        result.extend(level_values)
        current_level = next_level
        left_to_right = not left_to_right
    return result

no_of_nodes = int(input("Count of nodes: "))
node_relations = []

for _ in range(no_of_nodes):
    parent, child, side = input().split()
    node_relations.append((parent, child, side))

root = build_tree(node_relations)
traversal_result = zigzag_traversal(root)
print("Zigzag Traversal:", traversal_result)