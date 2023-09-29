# LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        self.headvalue = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.headvalue
        self.headvalue = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.headvalue == None:
            self.headvalue = new_node
        else:
            last_node = self.headvalue
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

    def display(self):
        if self.headvalue == None:
            print("Linked list_comprehensions is empty...")
        else:
            while self.headvalue is not None:
                print(self.headvalue.data)
                self.headvalue = self.headvalue.next


obj = singly_linked_list()

x = int(input(
    "Select your choice: \n 1. Insert At Beginning \n 2. Insert In Between \n 3. Insert at End \n 4. Print \n 5. Print and Exit \n"))

while x:
    if x == 1:
        number = int(input("Enter the data you want to add in this node: "))
        obj.insert_at_beginning(number)

    elif x == 2:
        node_number = int(input("Enter the node after you want to add this node: "))
        middle_node = obj.headvalue
        while node_number != 0:
            middle_node = obj.headvalue.next
            node_number -= 1

        number = int(input("Enter the data you want to add in this node: "))

        obj.insert_in_between(middle_node, number)

    elif x == 3:
        number = int(input("Enter the data you want to add in this node: "))
        obj.insert_at_end(number)

    elif x == 4:
        print("\n===========================\n")
        obj.display()
        print("\n===========================\n")

    elif x == 5:
        print("\n===========================\n")
        obj.display()
        print("\n===========================\n")
        break

    else:
        x = int(input(
            "Select correct choice from following: \n 1. Insert At Beginning \n 2. Insert In Between \n 3. Insert at End \n 4. Print \n 5. Print and Exit \n"))

    x = int(input(
        "Select your choice: \n 1. Insert At Beginning \n 2. Insert In Between \n 3. Insert at End \n 4. Print \n 5. Print and Exit \n"))