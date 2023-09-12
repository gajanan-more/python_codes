# STACK

class stack:
    def __init__(self):
        self.stk = []

    def push_stack(self):
        self.stk.append(int(input("Enter into the stack: ")))
        self.display()

    def pop_stack(self):
        if len(self.stk) == 0:
            print("Nothing to pop\n")
        else:
            print("Removing element from stack: ", self.stk[-1])
            self.stk.pop()
            self.display()

    def display(self):
        if len(self.stk) == 0:
            print("Nothing to display \n")
        else:
            print(self.stk)
            print("\n +++++++++++++ ")


obj = stack()

x = int(input("Select your choice: \n 1. Push \n 2. Pop \n 3. Print Stack \n 4. Print and Exit \n "))

while x:
    if x == 1:
        obj.push_stack()

    elif x == 2:
        obj.pop_stack()

    elif x == 3:
        obj.display()

    elif x == 4:
        obj.display()
        break

    else:
        int(input(
            "Select correct choice from following:  \n 1. Push \n 2. Pop \n 3. Print Stack \n 4. Print and Exit \n "))

    x = int(input("Select your choice: \n 1. Push \n 2. Pop \n 3. Print Stack \n 4. Print and Exit \n "))