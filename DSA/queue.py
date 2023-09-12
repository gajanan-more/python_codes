# QUEUE

class queue:
    def __init__(self):
        self.q = []

    def enqueue(self):
        self.q.append(int(input("Enter into the queue: ")))
        self.display()

    def dequeue(self):
        if len(self.q) == 0:
            print("Nothing to dequeue...")
        else:
            print("Removing element from queue: ", self.q[0])
            self.q.remove(self.q[0])
            self.display()

    def display(self):
        if len(self.q) == 0:
            print("Nothing to display...")
        else:
            print(self.q)
            print("\n +++++++++++++ ")


obj = queue()

x = int(input("Select your choice: \n 1. Enqueue \n 2. Dequque \n 3. Print Queue \n 4. Print and Exit \n "))

while x:
    if x == 1:
        obj.enqueue()

    elif x == 2:
        obj.dequeue()

    elif x == 3:
        obj.display()

    elif x == 4:
        obj.display()
        break

    else:
        int(input(
            "Select correct choice from following:  \n 1. Enqueue \n 2. Dequque \n 3. Print Queue \n 4. Print and Exit \n "))

    x = int(input("Select your choice: \n 1. Enqueue \n 2. Dequque \n 3. Print Queue \n 4. Print and Exit \n "))