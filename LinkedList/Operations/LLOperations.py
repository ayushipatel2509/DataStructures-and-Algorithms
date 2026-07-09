class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def printList(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next
    
    #Add node at end of linked list
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    # Remove node from end of Linked List
    def pop(self):
        # Case 1: List is Empty
        if self.head is None:
            return None
        
        # Case 2: If there is only one node in List
        if self.head.next is None:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node
        
        # Case 3: There are more than 1 node in the list
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp 
            temp = temp.next
        pre.next = None
        self.tail = pre
        self.length -= 1 
        return temp
    
    # Add node at front of linked list
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    # Remove node from beginnig of Linked list
    def pop_first(self):
        if self.head is None:
            return None
        else:
            currentNode = self.head
            self.head = self.head.next
            currentNode.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return currentNode
        
    # Get value by index
    def get(self, index):
        if index<0 or index >self.length:
            return None
        else:
            currentNode = self.head
            for _ in range(index):
                currentNode = currentNode.next
            return currentNode
        
    # Set value by index 
    def set(self, index, data):
        if index < 0 or index > self.length:
            return False
        else:
            currentNode = self.head
            for _ in range(index):
                currentNode = currentNode.next
            currentNode.data = data
            return True
        
    # Insert at a specific index
    def insert(self,index, data):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            self.prepend(data)
            return True
        if index == self.length:
            self.append(data)
            return True
        new_node = Node(data)
        currentValue = self.get(index-1)
        new_node.next = currentValue.next
        currentValue.next = new_node
        self.length += 1
        return True
    
    # Remove from specific index
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            result = self.pop_first()
            return result
        if index == self.length:
            result = self.pop()
            return result
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    # Reverse Linked List
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp 
            temp = after
    
    
        
    
    

my_linked_list = LinkedList(4)
my_linked_list.append(3)
my_linked_list.append(6)
my_linked_list.append(7)
#my_linked_list.prepend(1)
#popped_value = my_linked_list.pop()
#print("Popped Value: ", popped_value)
#popped_value_first = my_linked_list.pop_first()
#print("Pop from first:" , popped_value_first)
my_linked_list.insert(3,100)
my_linked_list.printList()
my_linked_list.remove(3)




print("Head: ",my_linked_list.head.data)
print("Tail :", my_linked_list.tail.data)
print("Length:", my_linked_list.length)
my_linked_list.printList()
print("Using get function:", my_linked_list.get(0))
print("Using set function:", my_linked_list.set(2,99))
my_linked_list.reverse()
my_linked_list.printList()





        