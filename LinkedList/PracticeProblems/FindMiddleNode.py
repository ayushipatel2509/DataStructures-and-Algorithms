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
        """
        Finds and returns the value of the middle node using 
        Floyd's Cycle-Finding (Tortoise and Hare) algorithm.
        
        How it works:
        1. Two pointers ('slow' and 'fast') start at the head.
        2. 'fast' moves 2 steps at a time, while 'slow' moves 1 step.
        3. Because 'fast' moves twice as fast, the moment 'fast' 
           reaches the end of the list, 'slow' will be perfectly 
           positioned exactly in the middle.
           
        Safety Checks:
        - 'fast is not None' handles even-lengthed lists.
        - 'fast.next is not None' handles odd-lengthed lists.
        """
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
        