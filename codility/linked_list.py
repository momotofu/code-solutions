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


    def delete(self, value):
        """Delete the first node with a given value."""
