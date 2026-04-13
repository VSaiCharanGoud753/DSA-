stack = []

def push():
    n = int(input("Enter the element in stack: "))
    stack.insert(0, n)

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        removed = stack.pop(0)
        print("Popped element:", removed)

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:")
        for element in stack:
            print(element)

while(1):
    print("\n----------- STACK MENU ------------------")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    print("----------------------------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice")