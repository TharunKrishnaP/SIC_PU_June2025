#Merge two sorted sll

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
    
    def create_sll_from_list(self):
        lt = input("Input: ").split(" -> ")
        lt.sort()
        for i in lt:
            node = Node(i)
            self.insert_node_rear(node)
        return self
    
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> " if temp.link else "")
            temp = temp.link
        
    def merge_sorted_sll(self,sll1,sll2):
        a = sll1.front
        b = sll2.front
        head = tail = None
        while a and b:
            if a.data <= b.data:
                node = a
                a = a.link
            else:
                node = b
                b = b.link
            if not head:
                head = tail = node
            else:
                tail.link = node
                tail = node
        remaining = a if a else b
        if head == None:
            head = remaining
        else:
            tail.link = remaining
        self.front = head
        return self      

sll1 = SLL().create_sll_from_list()
sll2 = SLL().create_sll_from_list()
merged_sll = SLL().merge_sorted_sll(sll1,sll2)
merged_sll.display()