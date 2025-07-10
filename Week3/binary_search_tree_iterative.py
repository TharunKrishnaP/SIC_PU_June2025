class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def insert_node(self,data):
        new_node = Node(data) # create a new Node object
        if self.root == None: # check if the tree is empty
            self.root = new_node
            return
        temp1 = self.root
        while True:
            if data < temp1.data:
                if temp1.left is None:
                    temp1.left = new_node
                    return
                temp1 = temp1.left
            else:
                if temp1.right is None:
                    temp1.right = new_node
                    return
                temp1 = temp1.right



    def in_order_traversal(self,temp):
        if temp == None:
            print("Empty tree")
            return
        self.in_order_traversal(temp.left)
        print(temp.data)
        self.in_order_traversal(temp.right)

    def pre_order_traversal(self,temp):
        if temp == None:
            print("Empty tree")
            return
        print(temp.data)
        self.in_order_traversal(temp.left)
        self.in_order_traversal(temp.right)

    def post_order_traversal(self,temp):
        if temp == None:
            print("Empty tree")
            return
        self.in_order_traversal(temp.left)
        self.in_order_traversal(temp.right)
        print(temp.data)

    def search_node(self,temp,target):
        found = False
        while temp!= None:
            if temp.data == target:
                return True
            found = self.search_node(temp.right,target)
            if found:
                return found
            found = self.search_node(temp.left,target)
        return found

class Menu:
    def __init__(self):
        self.choice = 0
    
    def is_tree_empty(self,bst):
        if bst.root == None:
            return True
        return False
    
    def menu(self,bst):
        match self.choice:
            case 1: 
                data = int(input("Enter value of node: "))
                bst.insert_node(data)
            case 2: 
                if self.is_tree_empty(bst):
                    return
                bst.pre_order_traversal
            case 3: 
                if self.is_tree_empty(bst):
                    return
                bst.in_order_traversal
            case 4: 
                if self.is_tree_empty(bst):
                    return
                bst.post_order_traversal
        
bst = BST()