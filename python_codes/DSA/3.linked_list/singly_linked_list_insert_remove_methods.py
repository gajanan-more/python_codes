# LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next

        last_node.next = new_node

    def insert_in_between(self, middle_node, data):
        if middle_node is None:
            print("Node is absent")
        else:
            new_node = Node(data)
            new_node.next = middle_node.next
            middle_node.next = new_node

    def remove_item(self, data):
        node = self.head

        if node is not None:
            if node.data == data and node.next == None:
                print("Only one element in the linked list_comprehensions and it is removed")
                self.head = None
                return

            elif node.data == data:
                self.head = node.next
                node = None

            else:
                while node is not None:
                    if node.data == data:
                        break

                    prev = node
                    node = node.next

            if self.head != None:
                prev.next = node.next
                node = None

    def display(self):
        if self.head == None:
            print("Linked list_comprehensions is empty...")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next


obj = singly_linked_list()

x = input(
    "Select your choice: \n 1. Insert At Beginning \n 2. Insert In Between \n 3. Insert at End \n 4. Remove Item \n 5. Print \n 6. Print and Exit \n")

valid_inputs = ['1', '2', '3', '4', '5', '6']

while x:
    if x in valid_inputs:

        if x == '1':
            number = int(input("Enter the data you want to add in this node: "))
            obj.insert_at_beginning(number)

        elif x == '2':
            node_number = int(input("Enter the node after you want to add this node: "))

            middle_node = obj.head

            while node_number != 1:
                middle_node = middle_node.next
                node_number -= 1

            number = int(input("Enter the data you want to add in this node: "))

            obj.insert_in_between(middle_node, number)

        elif x == '3':
            number = int(input("Enter the data you want to add in this node: "))
            obj.insert_at_end(number)

        elif x == '4':
            number = int(input("Enter the data you want to add in this node: "))
            obj.remove_item(number)

        elif x == '5':
            print("\n===========================\n")
            obj.display()
            print("\n===========================\n")

        elif x == '6':
            print("\n===========================\n")
            obj.display()
            print("\n===========================\n")
            break

    else:
        x = input(
            "Select your choice: \n 1. Insert At Beginning \n 2. Insert In Between \n 3. Insert at End \n 4. Remove Item \n 5. Print \n 6. Print and Exit \n")

    x = input(
        "Select your choice: \n 1. Insert At Beginning \n 2. Insert In Between \n 3. Insert at End \n 4. Remove Item \n 5. Print \n 6. Print and Exit \n")