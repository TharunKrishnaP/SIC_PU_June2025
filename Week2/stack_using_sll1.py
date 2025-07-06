class Student:
    def __init__(self,id,name,marks):
        self.id = id
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"ID : {self.id}  Name: {self.name}  Marks: {self.marks}"
    
class Node:
    def __init__(self,student):
        self.data = student 
        self.link = None
    

class Stack:
    def __init__(self):
        self.front = None
    
    def create_student(self):
        id = input("Enter ID: ")
        name = input("Enter name: ")
        marks = float(input("Enter your marks: "))
        student = Student(id,name,marks)
        return student
    
    def insert_node_front(self):
        student = self.create_student()      #Create student object
        node = Node(student)                        #Create a node object
        if self.front == None:
            self.front = node
            return
        node.link = self.front
        self.front = node
    
    def delete_node_front(self):
        if self.front is None:
            print("Empty queue")
            return
        print("Deleted:", self.front.data)
        self.front = self.front.link
    
    def display_stack(self):
        if self.front == None:
            print("Empty queue")
            return
        temp = self.front
        while temp!=None:
            if temp.link == None:
                print(temp.data)
            else:
                print(temp.data, "-->",end=" ")
            temp = temp.link
        
stack = Stack()
print("Operations: 1.Insert at front  2.Delete at front  3.Display stack  4.Exit")
choice = int(input("Enter choice: "))
while choice != 0:
    if choice == 1:
        stack.insert_node_front()
    elif choice == 2:
        stack.delete_node_front()
    elif choice == 3:
        stack.display_stack()
    else:
        print("invalid choice.")
    choice = int(input("Enter choice: "))

print("End of program.....")