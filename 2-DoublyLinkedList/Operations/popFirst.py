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
    
    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        return temp

         
    
   



my_linked_list = DoublyLinkedList(7)
my_linked_list.print()
my_linked_list.append(3)
my_linked_list.append(9)
my_linked_list.print()

my_linked_list.pop_first()
my_linked_list.print()



        