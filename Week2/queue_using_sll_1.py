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
    

class Queue:
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
    
    def delete_node_rear(self):
        if self.front == None:
            print("No elements to delete in queue")
            return
        if self.front.link == None:
            print(f"Deleted node = {self.front}")
            self.front = None
            return
        
        temp = self.front
        while temp.link.link != None:
            temp = temp.link                               #Traverse to last but one node
        print(f"Deleted node = {temp.link.data}")         
        temp.link = None                                   #Set the link of last second node to none
    
    def display_queue(self):
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

queue = Queue()
print(f"Operations: 1.Insert at front  2.Delete at rear  3.Display queue  0.Exit")
choice = int(input("Enter choice: "))
while choice != 0:
    if choice == 1:
        queue.insert_node_front()
        print("Node inserted successfully")
    elif choice == 2:
        queue.delete_node_rear()
        print("Node deleted successfully")
    elif choice == 3:
        queue.display_queue()
    else:
        print("Invalid choice")
    choice = int(input("Enter choice: "))
print("End of Program")