class stack:
    def __init__(self):
        self.l1 = []
        print("from Init")

    def push(self, item):
        self.l1.append(item)

    def pop_item(self):
        self.l1.pop()

    def display(self):
        print(self.l1)


obj = stack()

for i in range(3):
    y = int(input("Enter item"))
    obj.push(y)

obj.pop_item()
obj.display()

