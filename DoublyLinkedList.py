class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head is None

    def display_forward(self):
        ptr = self.head
        print("[", end=" ")
        while ptr:
            print("({}, {})".format(ptr.key, ptr.data), end=" ")
            ptr = ptr.next
        print("]")

    def display_backward(self):
        ptr = self.last
        print("[", end=" ")
        while ptr:
            print("({}, {})".format(ptr.key, ptr.data), end=" ")
            ptr = ptr.prev
        print("]")

    def insert_first(self, key, data):
        link = Node(key, data)
        if self.is_empty():
            self.last = link
        else:
            self.head.prev = link
        link.next = self.head
        self.head = link

    def insert_last(self, key, data):
        link = Node(key, data)
        if self.is_empty():
            self.last = link
        else:
            self.last.next = link
            link.prev = self.last
        self.last = link

    def delete_first(self):
        if self.is_empty():
            return None
        temp_link = self.head
        if self.head.next is None:
            self.last = None
        else:
            self.head.next.prev = None
        self.head = self.head.next
        return temp_link

    def delete_last(self):
        if self.is_empty():
            return None
        temp_link = self.last
        if self.head.next is None:
            self.head = None
        else:
            self.last.prev.next = None
        self.last = self.last.prev
        return temp_link

    def delete(self, key):
        current = self.head
        while current and current.key != key:
            current = current.next
        if current is None:
            return None
        if current == self.head:
            self.head = self.head.next
        else:
            current.prev.next = current.next
        if current == self.last:
            self.last = current.prev
        else:
            current.next.prev = current.prev
        return current

    def insert_after(self, key, new_key, data):
        current = self.head
        while current and current.key != key:
            current = current.next
        if current is None:
            return False
        new_link = Node(new_key, data)
        if current == self.last:
            new_link.next = None
            self.last = new_link
        else:
            new_link.next = current.next
            current.next.prev = new_link
        new_link.prev = current
        current.next = new_link
        return True

# Example usage
dll = DoublyLinkedList()
dll.insert_first(1, 10)
dll.insert_first(2, 20)
dll.insert_first(3, 30)
dll.insert_first(4, 1)
dll.insert_first(5, 40)
dll.insert_first(6, 56)
print("List (First to Last):")
dll.display_forward()
print()
print("List (Last to First):")
dll.display_backward()
print("List, after deleting first record:")
dll.delete_first()
dll.display_forward()
print("List, after deleting last record:")
dll.delete_last()
dll.display_forward()
print("List, insert after key(4):")
dll.insert_after(4, 7, 13)
dll.display_forward()
print("List, after delete key(4):")
dll.delete(4)
dll.display_forward()	
