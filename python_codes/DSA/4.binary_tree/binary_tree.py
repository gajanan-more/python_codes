class binary_tree:
    """Binary Tree class"""

    def __init__(self, data):
        """
        Initializes a binary tree node.

        Parameters:
        data (any): The data to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None

    def insert_into_tree(self, data):
        """
        Inserts a new node into the binary tree.

        Parameters:
        data (any): The data to be inserted into the tree.
        """
        if self.data is not None:
            if data <= self.data:
                if self.left is None:
                    self.left = binary_tree(data)
                else:
                    self.left.insert_into_tree(data)
            else:
                if self.right is None:
                    self.right = binary_tree(data)
                else:
                    self.right.insert_into_tree(data)
        else:
            self.data = data

    def in_order_traverse(self):
        """
        Performs in-order traversal of the binary tree. Left -> Root -> Right

        Returns:
        list: List of nodes visited during in-order traversal.
        """
        res = []
        if self.left:
            res = self.left.in_order_traverse()
        res.append(self.data)
        if self.right:
            res = res + self.right.in_order_traverse()
        return res

    def pre_order_traverse(self):
        """
        Performs pre-order traversal of the binary tree. Root -> Left -> Right

        Returns:
        list: List of nodes visited during pre-order traversal.
        """
        res = []
        res.append(self.data)
        if self.left:
            res = res + self.left.pre_order_traverse()
        if self.right:
            res = res + self.right.pre_order_traverse()
        return res

    def post_order_traverse(self):
        """
        Performs post-order traversal of the binary tree. Left -> Right -> Root

        Returns:
        list: List of nodes visited during post-order traversal.
        """
        res = []
        if self.left:
            res = self.left.post_order_traverse()
        if self.right:
            res = res + self.right.post_order_traverse()
        res.append(self.data)
        return res

    def display(self):
        """
        Displays the nodes of the binary tree.
        """
        if self.left:
            self.left.display()
        print(self.data),
        if self.right:
            self.right.display()


def options(check):
    if check == 1:
        if root_setup == 0:
            print("We are implementing binary tree. Create root first.\n")
            return '1'
        else:
            ops = input(
                "Select your choice: \n 1. Insert \n 2. In_Order Traverse \n 3. Pre_Order Traverse \n 4. Post_Order Traverse \n 5. Print and Exit \n=========================== \n")
            return str(int(ops) + 1)
    else:
        if root_setup == 0:
            print("Binary tree is empty")
            return False
        else:
            return True


root_setup = 0

ops = options(1)

valid_inputs = ['1', '2', '3', '4', '5', '6']

while True:
    if ops in valid_inputs:

        if ops == '1':
            number = int(input("Enter the root element of binary tree: "))
            print("\n===========================\n")
            root = binary_tree(number)
            root_setup = 1

        elif ops == '2':
            print("\n===========================\n")
            number = int(input("Enter the element you want to insert in binary tree: "))
            print("\n===========================\n")
            root.insert_into_tree(number)

        elif ops == '3':
            if options(2):
                print("\n============In Order Traverse===============\n")
                result = root.in_order_traverse()
                print(result)
                print("\n===========================\n")

        elif ops == '4':
            if options(2):
                print("\n============Pre Order Traverse===============\n")
                result = root.pre_order_traverse()
                print(result)
                print("\n===========================\n")

        elif ops == '5':
            if options(2):
                print("\n============Post Order Traverse===============\n")
                result = root.post_order_traverse()
                print(result)
                print("\n===========================\n")

        elif ops == '6':
            print("\n===========================\n")
            root.display()
            print("\n===========================\n")
            break

        else:
            ops = options(1)

        ops = options(1)
