# Reversal of Singly Linked List assuming input to be given as 1 -> 2 -> 3
class Node:
     def __init__(self,data):
        self.data = data
        self.link = None
class SLL:
    def __init__(self):
        self.front = None
    
    def insert_node_rear(self,node):
        if self.front == None:
            self.front = node
            return
        temp = self.front
        while temp.link !=None:
            temp = temp.link
        temp.link = node
    
    def create_sll_from_list(self,lt):
     for i in lt:
        node = Node(i)
        self.insert_node_rear(node)
    
    def reverse_sll(self):
        previous_node = None
        current_node = self.front
        while current_node != None:
            next_node = current_node.link
            current_node.link = previous_node
            previous_node = current_node
            current_node = next_node
        self.front = previous_node
        self.display()

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> " if temp.link else "")
            temp = temp.link

sll = SLL()
list1 = input("Input: ").split(" -> ")
sll.create_sll_from_list(list1)
sll.reverse_sll()