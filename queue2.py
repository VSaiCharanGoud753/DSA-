from collections import deque

class CheckoutQueue:
    def __init__(self):
        self.checkout_queue = deque()

    def add_customer(self, customer):
        print(f"Adding {customer} to the checkout queue.")
        self.checkout_queue.append(customer)

    def serve_customer(self):
        if not self.checkout_queue:
            print("No customers in the queue.")
        else:
            customer = self.checkout_queue.popleft()
            print(f"Serving {customer}.")

    def display_queue(self):
        if not self.checkout_queue:
            print("The checkout queue is empty.")
        else:
            print("Current checkout queue:")
            for customer in self.checkout_queue:
                print(customer)
queue = CheckoutQueue()
while True:
    print("\n---------CHECKOUT QUEUE MENU---------")
    print("1. Add customer")
    print("2. Serve customer")
    print("3. Display customers")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_name = input("Enter customer name: ")
        queue.add_customer(customer_name)

    elif choice == 2:
        queue.serve_customer()

    elif choice == 3:
        queue.display_queue()

    elif choice == 4:
        print("Exit")
        break

    else:
        print("Invalid choice")