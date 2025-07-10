# 2 SLL converges or not

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
    
    def is_sll_converge(self, sll1, sll2):
        visited_nodes = set()
        a = sll1.front
        while a:
            visited_nodes.add(a.data)
            a = a.link
        b = sll2.front
        while b:
            if b.data in visited_nodes:
                return "Yes"
            b = b.link
        return "No"


sll1 = SLL().create_sll_from_list()
sll2 = SLL().create_sll_from_list()
print(SLL().is_sll_converge(sll1,sll2))