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
    
    def is_palindrome(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        temp = slow
        before = None
        while temp is not None:
            after = temp.next
            temp.next = before 
            before = temp
            temp = after
        p1 = self.head
        p2 = before
        while p2 is not None:
            if p1.value != p2.value:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
print(my_linked_list.is_palindrome())