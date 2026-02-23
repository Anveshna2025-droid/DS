class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def remove(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
        else:
            print("Value not found!")

    def display(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# --- INPUT/OUTPUT SYSTEM ---
ll = LinkedList()

while True:
    print("\n1. Push (Start)  2. Append (End)  3. Remove  4. Display  5. Exit")
    choice = input("Enter choice (1-5): ")

    if choice == '1':
        val = input("Enter value to push: ")
        ll.push(val)
    elif choice == '2':
        val = input("Enter value to append: ")
        ll.append(val)
    elif choice == '3':
        val = input("Enter value to remove: ")
        ll.remove(val)
    elif choice == '4':
        ll.display()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")