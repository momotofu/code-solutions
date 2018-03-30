class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None

class MyQueue(object):
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return None

    def deque(self):
        data = self.head.data
        self.head = self.head.next
        self.length -= 1

        if self.head == None:
            self.tail = None
            self.length = 0

        return data

    def enque(self, value):
        node = Node(value)
        if self.tail:
            self.tail.next = node
        self.tail = node

        if not self.head:
            self.head = node

        self.length += 1


# Get number of lines
n = int(input())

# Create a queue instance
queue = MyQueue()

# gather instructions
# execute instructions upon gathering
for _ in range(n):
    params = [int(x) for x in input().split()]
    instruct = params[0]
    if instruct == 1:
        queue.enque(params[1])
    elif instruct == 2:
        queue.deque()
    else:
        print(queue.peek())
