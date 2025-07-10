class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def insert_node(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        temp1 = self.root
        temp2 = None
        while temp1 != None:
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node
        
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
            case 1: bst.insert_node()
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