import sys
def enqueue_rear():
    value = int(input("Enter value: "))
    queue.append(value)
    print(f"Element {value} added to queue.")

def dequeue_front():
    if queue == []:
        print("No elements to dequeue")
    else:
        print(f"Element {queue[0]} deleted from queue.")
        del queue[0]

def disp_queue():
    print("Front", end = " ")
    for i in queue:
        print(i, end = " ")
    print("Rear")

def invalid():
    print("Invalid choice")
    
def exit():
    print("End Of Program")
    sys.exit()
queue = []
ops = {
    1: enqueue_rear,
    2: dequeue_front,
    3: disp_queue,
    4: exit
}
print("Operations: 1.Enqueue 2.Dequeue 3.Display 4.Exit")
while True:
    choice = int(input("Enter choice: "))
    ops.get(choice,invalid)()