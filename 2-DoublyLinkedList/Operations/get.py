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
        self.length = 1

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
        self.length += 1
        return True
    
    def get(self,index):
        if index <0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current



my_linked_list = DoublyLinkedList(7)
my_linked_list.print()
my_linked_list.append(3)
my_linked_list.append(9)
my_linked_list.print()
print(my_linked_list.get(2))



        