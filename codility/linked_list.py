class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """Ad an element to end of list"""
        if not self.head:
            self.head = new_element
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_element

    def get_position(self, position):
        """Get an element from a particular position."""
        if position < 1:
            return self.head
        else:
            counter = 1 # set a counter to keep track of position
            cur = self.head

            while(cur and counter <= position):
                if counter == position:
                    return cur
                else:
                    counter += 1
                    cur = cur.next
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position."""
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            prev = self.get_position(position - 1)
            assert prev # ensure position is not out of bounds
            new_element.next = prev.next
            prev.next = new_element


    def delete(self, value):
        """Delete the first node with a given value."""
        cur = self.head
        prev = None
        while cur:
            if cur.value == value:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
            prev = cur
            cur = cur.next
