import sys
def push_into_stack():
    if len(st) >= stack_size:
        print("Stack overflow")
    else:
        value = int(input("Enter value: "))
        st.append(value)
def pop_from_stack():
    if st == []:
        print("Stack underflow")
    else:
        print("Popped element: ",st.pop())
def disp_stack():
    print("Top")
    for i in st[::-1]:
        print(i)
    print("Bottom")
def invalid():
    print("Invalid Choice")
def exit():
    print("End Of Program")
    sys.exit()
stack_size = int(input("Enter size of stack: "))
st = []
ops = {
    1: push_into_stack,
    2: pop_from_stack,
    3: disp_stack,
    4: exit
}
print("Operations: 1. Push  2. Pop  3. Display stack  4.Exit")
while True:
    choice = int(input("Enter choice: "))
    ops.get(choice,invalid)()