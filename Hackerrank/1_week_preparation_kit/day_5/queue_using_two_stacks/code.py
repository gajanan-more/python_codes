# Enter your code here. Read input from STDIN. Print output to STDOUT


def enqueue(item):
    queue.append(item)
    return


def dequeue():
    queue.pop(0)


def display():
    print(queue[0])


tests = int(input())

queue = []

while True:
    query = input()

    if '1' in query:
        enqueue(query.split(" ")[1])
        tests -= 1

    if query == '2':
        dequeue()
        tests -= 1

    if query == '3':
        display()
        tests -= 1

    if tests == 0:
        # display()
        break