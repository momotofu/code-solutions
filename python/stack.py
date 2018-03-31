class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
        self.length = 0

    def is_empty(self):
        return self.top == None

    def peek(self):
        return self.top.data

    def push(self, value):
        node = Node(value)
        if self.top != None:
            self.top.next = self.top
        self.top = node
        self.length += 1
        return self.length

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        self.length -= 1
        return data

if __name__ == '__main__':
    stack = Stack()
    print(stack)
    stack.push(1)
    print(stack.length)
    stack.push(3)
    print(stack.peek())
    print(stack.length)
    stack.push(1)
    stack.push(5)
    print(stack.length)
    print(stack.pop())
    print(stack.length)
