class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> " if temp.next else "\n")
            temp = temp.next

    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current is not None:
            num = num * 2 + current.value
            current = current.next
        return num


# Create a linked list for binary number 101
linked_list = LinkedList(1)
linked_list.append(0)
linked_list.append(1)
print(linked_list.binary_to_decimal())  # Output: 5

# Create a linked list for binary number 1101
linked_list2 = LinkedList(1)
linked_list2.append(1)
linked_list2.append(0)
linked_list2.append(1)
print(linked_list2.binary_to_decimal())  # Output: 13