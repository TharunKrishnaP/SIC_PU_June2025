class Circular_queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.c_queue = [None]*capacity
        self.front = self.rear = -1

    def enqueue(self):
        if (self.rear + 1) % self.capacity == self.front:
            print("Queue full")
            return
        data = int(input("Enter data: "))
        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.c_queue[self.rear] = data
        print(f"Value {data} inserted into queue")
    
    def dequeue(self):
        if self.front == -1:
            print("Empty queue")
            return
        removed_value = self.c_queue[self.front]
        self.c_queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Value {removed_value} deleted from queue")
    
    def display_queue(self):
        if self.front == -1:
            return "Empty queue"
        i = self.front
        print("Circular Queue: ")
        while True:
            print(self.c_queue[i], end = " ")
            if i == self.rear:
                break
            i = (i+1) % self.capacity
        print()

    def invalid(self):
        print("Invalid choice")

capacity = int(input("Enter capacity of queue: "))
circular_queue = Circular_queue(capacity)
queue_ops = { 1: circular_queue.enqueue,
              2: circular_queue.dequeue,
              3: circular_queue.display_queue }
choice = int(input("Enter choice: "))
while choice != 0:
    queue_ops.get(choice,circular_queue.invalid)()
    choice = int(input("Enter choice: "))
print("End of Program...........")