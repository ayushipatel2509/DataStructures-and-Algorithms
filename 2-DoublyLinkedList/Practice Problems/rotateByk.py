class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
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

    def append(self, value):
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

    def rotate(self, k):
        if self.length <= 1:
            return True
        k = k % self.length  # handles k=0, k=length, and k > length safely
        if k == 0:
            return True

        self.tail.next = self.head
        self.head.prev = self.tail

        new_tail = self.head
        for _ in range(k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        new_head.prev = None

        self.head = new_head
        self.tail = new_tail
        return True


my_linked_list = DoublyLinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.print()          # 1->2->3->4->5->None

my_linked_list.rotate(2)
my_linked_list.print()          # 3->4->5->1->2->None

my_linked_list.rotate(0)
my_linked_list.print()          # unchanged: 3->4->5->1->2->None

my_linked_list.rotate(5)
my_linked_list.print()          # unchanged: 3->4->5->1->2->None (5 = length, full rotation)