class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def print(self):
        current = self.head
        while current is not None:
            print(current.value, end="->")
            current = current.next
        print("None")

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return True
    
    def palindrome(self):
        p1 = self.head
        p2 = self.tail
        while p1 is not p2 and p1.prev is not p2:
            if p1.value != p2.value:
                return False
            p1 = p1.next
            p2 = p2.prev
        return True
        



my_linked_list = DoublyLinkedList(7)
my_linked_list.print()
my_linked_list.append(3)
my_linked_list.append(7)
my_linked_list.print()
print(my_linked_list.palindrome())



        