# LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class singly_linked_list:
    def __init__(self):
        self.headvalue = None

    def display(self):
        if self.headvalue == None:
            print("Linked list is empty...")
        else:
            while self.headvalue is not None:
                print(self.headvalue.data)
                self.headvalue = self.headvalue.next


n1 = singly_linked_list()

n1.headvalue = Node("Monday")

n2 = Node("Tuesday")

n3 = Node("Wednesday")

n1.headvalue.next = n2

n2.next = n3

n1.display()