class MyQueue(object):
    def __init__(self):
        self.items = []
        self.length = len(self.items)

    def peek(self):
        return self.items[0]

    def deque(self):
        front = self.items[0]
        if self.length > 0:
            self.items = self.items[1:]
            self.length -= 1
        else:
            self.items = []
        return front

    def enque(self, value):
        self.items.append(value)
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
