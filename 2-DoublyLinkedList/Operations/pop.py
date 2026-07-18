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
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        return temp




my_linked_list = DoublyLinkedList(7)
my_linked_list.print()

my_linked_list.append(3)
my_linked_list.append(9)
my_linked_list.append(2)
my_linked_list.print()

my_linked_list.pop()
my_linked_list.print()



        