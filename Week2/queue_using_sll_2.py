class Student:
    def __init__(self,id,name,marks):
        self.id = id
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"ID: {self.id}  Name: {self.name}  Marks: {self.marks}"

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
        marks = float(input("Enter marks: "))
        student = Student(id,name,marks)
        return student
    
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
    
    def insert_node_rear(self):
        student = self.create_student()
        node = Node(student)
        if self.front == None:
            self.front = node
            return
        temp = self.front
        while temp.link !=None:
            temp = temp.link
        temp.link = node
        print("Inserted succesfully")
        
    def delete_node_front(self):
        if self.front is None:
            print("Empty queue")
            return
        print("Deleted:", self.front.data)
        self.front = self.front.link


queue = Queue()
print("Operations: 1.Insert from rear  2.Delete from front  3.Display queue  0.Exit")
choice = int(input("Enter choice: "))
while choice != 0:
    if choice == 1:
        queue.insert_node_rear()
    elif choice == 2:
        queue.delete_node_front()
    elif choice == 3:
        queue.display_queue()
    else:
        print("invalid choice.")
    choice = int(input("Enter choice: "))

print("End of program.....")