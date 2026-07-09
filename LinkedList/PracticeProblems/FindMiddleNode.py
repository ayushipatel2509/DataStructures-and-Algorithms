class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self,value):
        if self.head is None:
            return False
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        return True
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow.value
    

linkedlist = LinkedList(4)
linkedlist.append(3)
linkedlist.append(9)
print(linkedlist.find_middle_node())
        