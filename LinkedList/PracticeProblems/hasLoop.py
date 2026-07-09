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
    
    def has_loop(self):
        """
        Detects if a cycle/loop exists in the linked list using 
        Floyd's Cycle-Finding Algorithm (The Tortoise and the Hare).
        
        How it works:
        1. Two pointers ('slow' and 'fast') start at the head of the list.
        2. The 'slow' pointer moves 1 step at a time, while the 'fast' 
           pointer moves 2 steps at a time.
        3. If there is NO loop: 
           The 'fast' pointer will eventually reach the end of the list 
           (None), breaking the while loop and returning False.
        4. If there IS a loop: 
           The list becomes an infinite circular track. Because 'fast' is 
           moving quicker, it will eventually "lap" the 'slow' pointer. 
           The moment they land on the exact same node (fast == slow), 
           a loop is confirmed, and it returns True.
        """
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
            
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False
